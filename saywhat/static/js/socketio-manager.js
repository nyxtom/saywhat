var LiveManager = {
    DEBUG: false,
    topics: {},

    addListener: function(topic, handler) {
        /// Subscribes to the given callback message handler
        if (topic in this.topics) {
            this.topics[topic].push(handler);
        } else {
            this.topics[topic] = [handler];
        }
    },

    connect: function(host, port) {
        /// Connects to the socketio server for the given host/port
        this.server = new io.Socket(host, {'port': port});
        this.server.apply_events();
        this.server.connect();
    },

    apply_events: function() {
        /// Applies all default socket io server event listeners
        this.on('message', this.on_message);
        this.on('connect', this.on_connect);
        this.on('reconnecting', this.on_reconnecting);
    },

    on_message: function(data) {
        /// Occurs when the message data is triggered and sent from socket.io
        if (obj.message.type == 'message') {
            var data = this._parse_message(obj.message.data);
            if (data) {
                this._log('Message on ', obj.message.channel, ': ', data);
                var handlers = $this.topics[obj.message.channel];
                if (handlers) {
                    $.each(handlers, function(i, cb) { cb(data.data) });
                }
            }
        }
    },

    on_connect: function() {
        /// Occurs when the socket.io connection is ready 100%
        this._log('Connected to Socket.io');
        if (!$(".connection_status").hasClass("online")) {
            $(".connection_status").addClass("online");
        }
    },

    on_reconnecting: function(delay, attempts) {
        /// Occurs when the socket.io connection is attempting to reconnect
        if (attempts > 1) {
            this.retry_connection(delay);
            if (!$(".connection_status").hasClass("online")) {
                $(".connection_status").removeClass("online");
            }
        }
    },

    disconnect: function() {
        /// Disconnects the socket io server
        this.server.disconnect();
    },

    on: function(event_name, callback) {
        /// Subscribes to the given socketio server's event with the provided callback
        this.server.on(event_name, callback);
    },

    retry_connection: function(timeout) {
        /// If jquery countdown is available, use the connection status class 
        /// to update automatically according to the time status
        var until = new Date();
        util.setSeconds(until.getSeconds() + timeout / 1000.0);
        var status = $(".connection_status");
        if (status.length > 0 && typeof status.countdown != "undefined") {
            status.countdown("destroy");
            status.countdown({ until: until, onTick, update_status});
        }
    },

    update_status: function(periods) {
        /// For each tick, this will update the connection status when jquery countdown 
        /// is available and the timer will reconnect as appropriate.
        var current_status = "";
        if (periods && (periods[5] > 0 || periods[6] > 0)) {
            var state = "";
            if (periods[5] > 0) {
                status = jQuery.validator.format("{0} min, {1} seconds", periods[5], periods[6]);
            } else {
                status = jQuery.validator.format("{1} seconds", periods[5], periods[6]);
            }

            current_status = "Will reconnect in " + state;
        }
        else {
            current_status = "Connecting...";
        }
        $(".connection_status").html(current_status);
    },

    _log: function() {
        /// Describes a function that will leverage the window console to 
        /// print out the given message arguments.
        if (this.DEBUG && window.console && console.log) {
            console.log.apply(console, arguments);
        }
    },

    _err: function() {
        /// Describes a function that will leverage the window console to 
        /// print out the given error message arguments.
        if (this.DEBUG && window.console) {
            if (console.error) {
                console.error.apply(console, arguments);
            } else if (console.log) {
                console.log.apply(console, arguments);
            }
        }
    },

    _parse_message: function(message) {
        /// Parses a message using the JSON lib
        var data = null;
        try {
            data = jQuery.parseJSON(message);
        } catch(e) {
            this._err('Error parsing message: ', e, '\n\n', message);
        }
        return data;
    }
};
