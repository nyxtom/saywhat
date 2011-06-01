from django.conf import settings
from redis import Redis
from gevent.greenlet import Greenlet
from django.http import HttpResponse

REDIS_HOST = getattr(settings, 'REDIS_HOST', 'localhost')

def _subscribe_listener(socketio, channel):
    """
    Peforms a block and listen for new messages
    to be published to redis. Since coroutines are
    being used, this method can block on listen()
    without interrupting the rest of the site.
    """
    red = Redis(REDIS_HOST)
    red.subscribe(channel)
    for i in red.listen():
        socketio.send({'message': i})

def socketio(request):
    """
    Handles the appropriate subscribe message
    from the client and spawns off greenlet coroutines
    to monitor messages from redis.
    """
    socketio = request.environ['socketio']

    while True:
        message = socketio.recv()

        if len(message):
            message = message[0].split(':')

            if message[0] == 'subscribe':
                g = Greenlet.spawn(_subscribe_listener, socketio, message[1])

    return HttpResponse()
