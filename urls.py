from django.conf.urls.defaults import patterns, include, url
from live.urls import urlpatterns as live_urls
from main.urls import urlpatterns as main_urls

urlpatterns = patterns('',)
urlpatterns += main_urls
urlpatterns += live_urls
