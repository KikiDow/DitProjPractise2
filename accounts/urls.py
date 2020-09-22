from django.conf.urls import url, include
from .views import logout, login, profile, register

#url patterns
urlpatterns = [
    url(r'^logout/$', logout, name='logout'),
    url(r'^login/$', login, name='login'),
    url(r'^profile/$', profile, name='profile'),
    url(r'^register/$', register, name='register'),
]
