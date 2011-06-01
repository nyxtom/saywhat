from uuid import uuid1
from redis import Redis
from django.conf import settings
from django.utils import simplejson

REDIS_HOST = getattr(settings, 'REDIS_HOST', 'localhost')

def send_message(channel, data):
    """
    Publishes a message to redis on the given channel (key) with the given data.
    """
    uid = uuid1().hex
    envelope = {'id': uid, 'data': data}
    red = Redis(REDIS_HOST)
    red.publish(channel, simplejson.dumps(envelope))
