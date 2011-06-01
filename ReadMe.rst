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
If you're using my shelter script you can create a virtualenv and setup
the project in no time and start hacking around with all the components.

Add `shelter <https://gist.github.com/975467>`_ to your ~/.bashrc (just a
simple alias to mkvirtualenv --no-site-packages that I use frequently)::

    shelter saywhat
    git clone http://git@github.com:nyxtom/saywhat.git
    cd saywhat && pip install -r requirements.txt
::


Scripts and Helpers
===================
Firstly you will need to source the commands to use them::

    source scripts/helpers
::

Various helpers were used to do common things like starting up and
shutting down supervisor, running acceptance tests, unit testing,
simple process kills, silent start-ups...etc. 

To see a list of the
commands that you can use with this project run the command::

    askthor
::


**:)**
