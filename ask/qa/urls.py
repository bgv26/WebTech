from django.conf.urls import patterns, url
from views import *

urlpatterns = patterns('',
    url(r'^$', index, name='index'),
    url(r'^login/$', test),
    url(r'^signup/$', test),
    url(r'^question/(?P<quest_id>\d+)/$', question, name='question'),
    url(r'^ask/', ask, name='ask'),
    url(r'^popular/$', popular, name='popular'),
    url(r'^new/$', test),
    url(r'^answer/$', answer, name='answer'),
)
