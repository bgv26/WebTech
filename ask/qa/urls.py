from django.conf.urls import patterns, url
from views import *

urlpatterns = patterns('',
    url(r'^$', index),
    url(r'^login/$', test),
    url(r'^signup/$', test),
    url(r'^question/(?P<id>\d+)/$', question, name='question'),
    url(r'^ask/', test),
    url(r'^popular/$', popular),
    url(r'^new/$', test),
)
