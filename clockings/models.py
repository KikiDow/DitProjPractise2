from django.db import models
from django.utils import timezone
from .utils import ChoiceEnum
from django.contrib.auth.models import User
from datetime import datetime
from django.contrib import messages
# Create your models here.


class PersonalDetails(models.Model):
	address_1 = models.CharField(max_length=100)
	address_2 = models.CharField(max_length=100)
	
	class Counties(ChoiceEnum):
	    # Only limited number of counties selected to demonstrate functionality.
            DUBLIN = 'Dublin'
            KILDARE = 'Kildare'
            CORK = 'Cork'
            MEATH = 'Meath'
            LAOIS = 'Laois'
		
	county = models.CharField(max_length=15, choices=Counties.choices(), default='None')
	contact_number = models.CharField(max_length=12, blank=True, null=True)
	personal_email = models.EmailField(blank=True, null=True) #Check exact syntax
	
	officer = models.ForeignKey(User, related_name='officer', on_delete=models.CASCADE)
	last_updated = models.DateTimeField(blank=True, null=True)
	
	def __unicode__(self):
	    return self.county
	
	def __str__(self):
	    return self.county


class Clocking(models.Model):
	officer_id = models.ForeignKey(User,related_name='officer_id', on_delete=models.CASCADE)
	number_of_clockings = models.IntegerField(default=0)
	clocking_in_time = models.DateTimeField(blank=True, null=True)
	clocking_out_time = models.DateTimeField(blank=True, null=True)
	lunch_out_time = models.DateTimeField(blank=True, null=True)
	lunch_in_time = models.DateTimeField(blank=True, null=True)
	clocking_date = models.DateField(auto_now=True)
	
	def __unicode__(self):
		return self.clocking_in_time
		
		
	def __str__(self):
		return str(self.clocking_in_time)
		
	def updateCorrectClocking(self, request):
		if self.number_of_clockings == 0:
			self.clocking_in_time = datetime.now()
			print("Clock In: " + str(self.clocking_in_time))
			messages.success(request, "Clock In completed.")
		elif self.number_of_clockings == 1:
			self.lunch_out_time = datetime.now()
			print("Lunch Out: " + str(self.lunch_out_time))
			messages.success(request, "Lunch Out clock completed.")
		elif self.number_of_clockings == 2:
			self.lunch_in_time = datetime.now()
			print("Lunch In: " + str(self.lunch_in_time))
			messages.success(request, "Lunch In clock completed.")
		else:
			self.clocking_out_time = datetime.now()
			print("Clock Out: " + str(self.clocking_out_time))
			messages.success(request, "Clock Out completed.")
		self.number_of_clockings += 1
		return self.save()
	
	"""
	def checkClockingDate(self, request):
		user = request.user
		todaysDate = datetime.datetime.now()
		clock_for_today = Clocking.objects.get(officer_id=user).get(todaysDate.strftime("%x"))
		if clock_for_today == True and self.number_of_clockings > 0:
			clock_for_today.updateCorrectClocking()
		else:
			clock_for_today = Clocking(officer_id=user)
			clock_for_today.save()
			clock_for_today.updateCorrectClocking(request)
		return self.save()
	"""	
	
	