from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('',
    url(r'^socket\.io', 'apps.live.views.socketio', name='socketio'),
)
