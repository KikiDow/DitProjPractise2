from django.conf.urls import url, include
from .views import landing_page, view_personal_details, create_personal_details, edit_personal_details, clocking_page, clock, remote_clocking_page, remote_clock, manual_clocking, view_manual_clock, view_submitted_manual_clockings, accept_manual_clock, reject_manual_clock

urlpatterns = [
    url(r'^$', landing_page, name='index'),
    url(r'^view_personal_details/$', view_personal_details, name='view_personal_details'),
    url(r'^create_personal_details/$', create_personal_details, name='create_personal_details'),
    url(r'^(?P<pk>\d+)/edit_personal_details/$', edit_personal_details, name='edit_personal_details'),
    url(r'^clocking_page/$', clocking_page, name='clocking_page'),
    url(r'^clock/$', clock, name='clock'),
    url(r'^remote_clocking_page/$', remote_clocking_page, name='remote_clocking_page'),
    url(r'^remote_clock/$', remote_clock, name='remote_clock'),
    url(r'^manual_clocking/$', manual_clocking, name='manual_clocking'),
    url(r'^(?P<pk>\d+)/$', view_manual_clock, name='view_manual_clock'),
    url(r'^view_submitted_manual_clockings/$', view_submitted_manual_clockings, name='view_submitted_manual_clockings'),
    url(r'^(?P<pk>\d+)/accept_manual_clock/$', accept_manual_clock, name='accept_manual_clock'),
    url(r'^(?P<pk>\d+)/reject_manual_clock/$', reject_manual_clock, name='reject_manual_clock'),
]