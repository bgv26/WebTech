from django.conf.urls import patterns, include, url
import qa.views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ask.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'views.test'),
    url(r'^login/$', 'views.test'),
    url(r'^signup/$', 'views.test'),
    url(r'^question/\d+/$', 'views.test'),
    url(r'^ask/$', 'views.test'),
    url(r'^popular/$', 'views.test'),
    url(r'^new/$', 'views.test'),
)
