from django import forms
from .models import PersonalDetails, Clocking

class PersonalDetailsForm(forms.ModelForm):
    class Meta:
        model = PersonalDetails
        fields = ('address_1', 'address_2', 'county', 'contact_number', 'personal_email')
        

class ClockingForm(forms.ModelForm):
    class Meta:
        model = Clocking
        fields = ()