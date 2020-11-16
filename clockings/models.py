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
	
	class RosterSide(ChoiceEnum):
    		A = 'A'
    		B = 'B'
	
	class Counties(ChoiceEnum):
	    # Only limited number of counties selected to demonstrate functionality.
            DUBLIN = 'Dublin'
            KILDARE = 'Kildare'
            CORK = 'Cork'
            MEATH = 'Meath'
            LAOIS = 'Laois'
    		
	county = models.CharField(max_length=15, choices=Counties.choices(), default='None')
	roster_side = models.CharField(max_length=2, choices=RosterSide.choices(), default='None')
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
	clocking_in_time = models.TimeField(blank=True, null=True)
	clocking_out_time = models.TimeField(blank=True, null=True)
	lunch_out_time = models.TimeField(blank=True, null=True)
	lunch_in_time = models.TimeField(blank=True, null=True)
	clocking_date = models.DateField(blank=True, null=True)
	
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
	

class RemoteClock(models.Model):
	remote_clock_officer_id = models.ForeignKey(User,related_name='remote_clock_officer_id', on_delete=models.CASCADE)
	remote_number_of_clockings = models.IntegerField(default=0)
	#Remote Clocking In
	remote_clock_in_location = models.CharField(max_length=200, blank=True, null=True)
	remote_clocking_in_time = models.DateTimeField(blank=True, null=True)
	#Remote Lunch Out
	remote_lunch_out_location = models.CharField(max_length=200, blank=True, null=True)
	remote_lunch_out_time = models.DateTimeField(blank=True, null=True)
	#Remote Lunch In
	remote_lunch_in_location = models.CharField(max_length=200, blank=True, null=True)
	remote_lunch_in_time = models.DateTimeField(blank=True, null=True)
	#Remote Clocking Out
	remote_clock_out_location = models.CharField(max_length=200, blank=True, null=True)
	remote_clocking_out_time = models.DateTimeField(blank=True, null=True)
	
	remote_clocking_date = models.DateTimeField(auto_now=True)
	
	def __str__(self):
		return f"User clocked in at {self.remote_clock_in_location} on {self.remote_clocking_date} ."
		
	def updateCorrectRemoteClocking(self, request):
		if self.remote_number_of_clockings == 0:
			self.remote_clocking_in_time = timezone.now()
			#self.remote_clock_in_location = ???
		elif self.remote_number_of_clockings == 1:
			self.remote_lunch_out_time = timezone.now()
			#self.remote_lunch_out_location = ???
		elif self.remote_number_of_clockings == 2:
			self.remote_lunch_in_time = timezone.now()
			#self.remote_lunch_in_location = ???
		elif self.remote_number_of_clockings == 3:
			self.remote_clocking_out_time = timezone.now()
		else:
			messages.success(request, "You have completed all clockings for this date.")
			#self.remote_clock_out_location = ???
		self.remote_number_of_clockings += 1
		return self.save()
		
class ManualClocking(models.Model):
	mc_officer_id = models.ForeignKey(User,related_name='mc_officer_id', on_delete=models.CASCADE)
	clocking_date = models.DateField(blank=False, null=False)
	clocking_in_time = models.TimeField(blank=False, null=False)
	clocking_out_time = models.TimeField(blank=False, null=False)
	lunch_out_time = models.TimeField(blank=False, null=False)
	lunch_in_time = models.TimeField(blank=False, null=False)
	reason_for_missed_clocking = models.CharField(max_length=200, blank=False, null=False)
	checked_by_validator = models.BooleanField(default=False)
	validator_id = models.ForeignKey(User, related_name='validator_id', on_delete=models.CASCADE, blank=True, null=True)
	accept_reject_clock = models.BooleanField(default=False)
	reason_manual_clock_rejected = models.TextField(max_length=250, blank=True, null=True)
	
	
	def __unicode__(self):
		return self.clocking_date
		
		
	def __str__(self):
		return str(self.clocking_date)
		

	
	
	