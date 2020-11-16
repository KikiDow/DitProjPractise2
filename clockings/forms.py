from django import forms
from .models import PersonalDetails, Clocking, RemoteClock, ManualClocking

class PersonalDetailsForm(forms.ModelForm):
    class Meta:
        model = PersonalDetails
        fields = ('address_1', 'address_2', 'county', 'contact_number', 'personal_email')
        

class ClockingForm(forms.ModelForm):
    class Meta:
        model = Clocking
        fields = ()
        

class RemoteClockForm(forms.ModelForm):
    class Meta:
        model = RemoteClock
        fields = ()
        
class ManualClockingForm(forms.ModelForm):
    
    clocking_date = forms.DateField(required=True, widget=forms.DateInput(attrs={'type': 'date'}))
    clocking_in_time = forms.TimeField(required=True, widget=forms.TimeInput(attrs={'type': 'time'}))
    lunch_out_time = forms.TimeField(required=True, widget=forms.TimeInput(attrs={'type': 'time'}))
    lunch_in_time = forms.TimeField(required=True, widget=forms.TimeInput(attrs={'type': 'time'}))
    clocking_out_time = forms.TimeField(required=True, widget=forms.TimeInput(attrs={'type': 'time'}))
    reason_for_missed_clocking = forms.CharField(required=True, widget=forms.Textarea())

    class Meta:
        model = ManualClocking
        fields = ('clocking_date', 'clocking_in_time', 'lunch_out_time', 'lunch_in_time', 'clocking_out_time', 'reason_for_missed_clocking')
        
class ManualClockAcceptRejectForm(forms.ModelForm):
    
    accept_reject_clock = forms.BooleanField(required=False, widget=forms.CheckboxInput())
    reason_manual_clock_rejected = forms.CharField(max_length=250, required=True, widget=forms.Textarea())
        
    class Meta:
        model = ManualClocking
        fields = ('accept_reject_clock', 'reason_manual_clock_rejected')
        