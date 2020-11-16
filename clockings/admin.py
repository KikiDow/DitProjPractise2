from django.contrib import admin
from .models import PersonalDetails, Clocking, RemoteClock

# Register your models here.
admin.site.register(PersonalDetails)
admin.site.register(Clocking)
admin.site.register(RemoteClock)
