from django.conf.urls.defaults import patterns, include, url
from apps.live import urls as live_urls

urlpatterns = patterns('',
)

urlpatterns += live_urls
