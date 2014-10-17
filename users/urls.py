from django.conf.urls import patterns, url

urlpatterns = patterns('users.views',
    url(r'^signup/$', 'signup', name='signup'),
)
