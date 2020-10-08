from django.conf.urls import url, include
from .views import landing_page, view_personal_details, create_personal_details, edit_personal_details, clocking_page, clock

urlpatterns = [
    url(r'^$', landing_page, name='index'),
    url(r'^view_personal_details/$', view_personal_details, name='view_personal_details'),
    url(r'^create_personal_details/$', create_personal_details, name='create_personal_details'),
    url(r'^(?P<pk>\d+)/edit_personal_details/$', edit_personal_details, name='edit_personal_details'),
    url(r'^clocking_page/$', clocking_page, name='clocking_page'),
    url(r'^clock/$', clock, name='clock'),
]