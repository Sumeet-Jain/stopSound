from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'stopSound.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^auth/', include('django.contrib.auth.urls')),
    url(r'^auth/', include('users.urls')),
    url(r'^contacts/', include('contacts.urls')),
    url(r'^access_denied/$', 'stopSound.views.denied', name="access_denied"),
    url(r'^$', 'stopSound.views.home', name='home')
)
