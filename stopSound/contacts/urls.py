from django.conf.urls import patterns, url

urlpatterns = patterns('contacts.views',
        url(r'^view_all/$', 'contacts', name='view_contacts'),
        url(r'^settings/$', 'serialize_settings', name='get_settings'),
        url(r'^send_messages/$', 'send_messages', name='send_messages'),
        url(r'^add_contact/$', 'add_contact', name='add_contact'),
)
