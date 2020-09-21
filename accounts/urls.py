from django.conf.urls import url, include
from .views import logout

#url patterns
urlpatterns = [
    url(r'^logout/$', logout, name='logout'),
]
