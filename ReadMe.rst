Say What? GEvent, Django, Socket.io and Redis
#############################################

I love bringing technologies together that makes things simple to do
really neat and fun things like when dealing with live feedback!


Projects Used
==========================
Testing is done with
`nose <http://somethingaboutorange.com/mrl/projects/nose/1.0.0/>`_ and the
`sure <https://github.com/gabrielfalcao/sure>`_ testing tools.

Additionally, `redis <http://redis.io>`_, 
`gevent <http://www.gevent.org/>`_, `socket.io <http://socket.io>`_, 
and especially `django <http://djangoproject.org/>`_.


Setup and Testing
=========================
You will need to make sure you have a version of nginx that is patched
with the tcp proxy module maintained by 
`yaoweibin <http://github.com/yaoweibin>`_::

    https://github.com/yaoweibin/nginx_tcp_proxy_module

Or, my great friend Gabriel Falcao created a simple brew formula::

    https://gist.github.com/1007028

You can simple run::

    brew install https://gist.github.com/1007028

If you're using my shelter script you can create a virtualenv and setup
the project in no time and start hacking around with all the components.

Add `shelter <https://gist.github.com/975467>`_ to your ~/.bashrc (just a
simple alias to mkvirtualenv --no-site-packages that I use frequently)::

    shelter saywhat
    git clone http://git@github.com:nyxtom/saywhat.git
    cd saywhat && pip install -r requirements.txt


Scripts and Helpers
===================
Firstly you will need to source the commands to use them::

    source scripts/helpers

Various helpers were used to do common things like starting up and
shutting down supervisor, running acceptance tests, unit testing,
simple process kills, silent start-ups...etc. 

To see a list of the
commands that you can use with this project run the command::

    askthor

Running it
==========
After you've reviewed and got things setup, run the below::

    runthor

**:)**
