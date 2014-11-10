from django.conf.urls import patterns, url

urlpatterns = patterns('contacts.views',
        url(r'^view_all/$', 'contacts', name='view_contacts'),
        url(r'^settings/$', 'serialize_settings', name='get_settings'),
        url(r'^send_messages/$', 'send_messages_json', name='send_messages'),
        url(r'^maybe_send/$', 'before_send_messages', name='before_send_messages'),
        url(r'^add_contact/$', 'add_contact', name='add_contact'),
        url(r'^change_actives/$', 'change_actives', name='change_actives'),
        url(r'^edit/(\d+)/$', 'edit_contact', name='edit_contact'),
        url(r'^get_actives/$', 'get_actives', name='get_actives'),
        url(r'^view_settings/$', 'choose_settings', name='view_settings'),
        url(r'^update_settings/$', 'update_settings', name='update_settings'),
        url(r'^advanced_settings/$', 'choose_advanced_settings', name='advanced_settings'),
)
