from django.shortcuts import render, redirect, HttpResponseRedirect, get_object_or_404, reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from .models import PersonalDetails, Clocking
from .forms import PersonalDetailsForm
import datetime

# Create your views here.
def landing_page(request):
    return render(request, "landing_page.html")
    

@login_required()
def view_personal_details(request):
    user = request.user
    personal_details_check = PersonalDetails.objects.filter(officer=user)
    #print(personal_details_check)

    if personal_details_check.exists():
        personal_details = PersonalDetails.objects.get(officer=user)
        info_message = ""
        personal_details_exist = True
        
        print("INFO 2")
    else:
        info_message = "You have not yet filled out any personal details. Please create new details below."
        personal_details_exist = False
        personal_details = None
        print("INFO 1")
        
    args = {'personal_details': personal_details, 'info_message': info_message, 'personal_details_exist': personal_details_exist}
    return render(request, "view_personal_details.html", args)
    
@login_required()
def create_personal_details(request):
    if request.method == "POST":
        create_personal_details_form = PersonalDetailsForm(request.POST, request.FILES)
        if create_personal_details_form.is_valid():
            create_personal_details_form.instance.officer = request.user
            personal_details = create_personal_details_form.save()
            messages.success(request, 'You have successfully filled out your personal details.')
            
            args = {'personal_details': personal_details}
            return redirect(view_personal_details)
    else:
        create_personal_details_form = PersonalDetailsForm()
        
    return render(request, "create_personal_details.html", {'create_personal_details_form': create_personal_details_form})
    
@login_required()
def edit_personal_details(request, pk):
    """
    dt_current_time = datetime.datetime.now()
    print("Datetime time: " + str(dt_current_time))
    print("Date: " + str(dt_current_time.strftime("%x")))
    """
    personal_details = get_object_or_404(PersonalDetails, pk=pk) if pk else None
    user = request.user
    if request.method == "POST":
        edit_personal_details_form = PersonalDetailsForm(request.POST, request.FILES, instance=personal_details)
        if edit_personal_details_form.is_valid():
            edit_personal_details_form.instance.officer = request.user
            personal_details = edit_personal_details_form.save()
            messages.success(request, 'You have successfully updated your personal details..')

            return redirect(view_personal_details)
    else:
        edit_personal_details_form = PersonalDetailsForm(instance=personal_details)
        

    return render(request, "edit_personal_details.html", {'personal_details': personal_details, 'edit_personal_details_form': edit_personal_details_form})
    

@login_required()
def clocking_page(request):
    return render(request, "clocking_page.html")
    
    
@login_required()
def clock(request):
    if request.method == "POST":
        user = request.user
        todaysDate = datetime.datetime.now()
        print(todaysDate)
        clock_for_todaysDate_check = Clocking.objects.filter(officer_id=user).filter(clocking_date=todaysDate)
        print(clock_for_todaysDate_check)
        if clock_for_todaysDate_check.exists():
            print("Clocking exists.")
            clock_for_today = Clocking.objects.get(officer_id=user, clocking_date=todaysDate) #.get(clocking_date=todaysDate.strftime("%x"))
            if clock_for_today.number_of_clockings > 0:
                clock_for_today.updateCorrectClocking(request)
        else:
            print("No clocking exists for this date.")
            clock_for_today = Clocking(officer_id=user)
            #clock_for_today.save()
            clock_for_today.updateCorrectClocking(request)
        clock_for_today.save()
    return redirect("profile")



    
    