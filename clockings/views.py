from django.shortcuts import render, redirect, HttpResponseRedirect, get_object_or_404, reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from .models import PersonalDetails, Clocking, RemoteClock, ManualClocking
from .forms import PersonalDetailsForm, ManualClockingForm, ManualClockAcceptRejectForm
import datetime
from geopy.geocoders import Nominatim
from .utils import getCurrentLocationFromGeoIP, get_ip_address
from ipaddress import IPv4Address
import folium
from IPython.core.display import HTML
from django.conf import settings


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
    t = settings.GLOBAL_START_DATE
    print(t)
    return render(request, "clocking_page.html")
    
    
@login_required()
def clock(request):
    if request.method == "POST":
        user = request.user
        todaysDate = datetime.datetime.now()
        #print(todaysDate)
        clock_for_todaysDate_check = Clocking.objects.filter(officer_id=user).filter(clocking_date=todaysDate)
        #print(clock_for_todaysDate_check)
        if clock_for_todaysDate_check.exists():
            print("Clocking exists.")
            clock_for_today = Clocking.objects.get(officer_id=user, clocking_date=todaysDate) #.get(clocking_date=todaysDate.strftime("%x"))
            #if clock_for_today.number_of_clockings > 0:
            clock_for_today.updateCorrectClocking(request)
        else:
            print("No clocking exists for this date.")
            clock_for_today = Clocking(officer_id=user, clocking_date=todaysDate)
            #clock_for_today.save()
            clock_for_today.updateCorrectClocking(request)
        clock_for_today.save()
    return redirect("profile")


@login_required()
def remote_clocking_page(request):
    geolocator = Nominatim(user_agent='clockings')
    if request.method == "GET":
        lat = request.GET.get('latitude', None)
        lon = request.GET.get('longitude', None)
        print(lat)
        if lat is not None and lon is not None:
            pointA = (lat, lon)
            m = folium.Map(location=pointA, width=600, height=400, zoom_start=16)
            folium.Marker([lat, lon], tooltip='Click here for more.',
                    icon=folium.Icon(color='purple')).add_to(m)
            m = m._repr_html_()
            return render(request, "remote_clocking_page.html", {'myMap': m })
        else:
            return render(request, "remote_clocking_page.html")
    """
    lat = request.GET.get("latitude")
    lon = request.GET.get("longitude")
    print(lat)
    if request.is_ajax and lat is not None:
        pointA = (lat, lon)
        m = folium.Map(location=pointA, width=600, height=400, zoom_start=16)
        folium.Marker([lat, lon], tooltip='Click here for more.',
                    icon=folium.Icon(color='purple')).add_to(m)
        m = m._repr_html_()
        return render(request, "remote_clocking_page.html", {'myMap': m })
    else:
        lat_b = 53.038264
        lon_b = -7.283749
        pointB = (lat_b, lon_b)
        m = folium.Map(location=pointB, width=600, height=400, zoom_start=16)
        folium.Marker([lat_b, lon_b], tooltip='Click here for more.',
                    icon=folium.Icon(color='purple')).add_to(m)
        m = m._repr_html_()
        return render(request, "remote_clocking_page.html", {'myMap': m })
    """    
        
    #ip = IPv4Address("72.14.207.99")
    #ip = '217.183.255.255' #Cork
    #ip = '192.168.58.1' #own2
    #ip = '172.31.13.94' #socket result
    """ip =  get_ip_address(request)
    print(ip)
    country, city, lat, lon = getCurrentLocationFromGeoIP(ip)
    
    print("Location country is " + str(country))
    print("Location city is " + str(city))
    print("Location latitude:  " + str(lat))
    print("Location longitude: " + str(lon))
    """
    #test_lat = 53.1653551
    #test_lon = -6.908424
    #pointB = (test_lat, test_lon)
    
    #location = geolocator.geocode(test_lat, test_lon)
    #print("### ", location)
    """l_lat = lat
    l_lon = lon
    pointA = (l_lat, l_lon)
    """
    """
    m = folium.Map(location=pointB, width=600, height=400, zoom_start=16)
    folium.Marker([test_lat, test_lon], tooltip='Click here for more.',
                    icon=folium.Icon(color='purple')).add_to(m)
    m = m._repr_html_()
    , {'myMap': m }
    """
    #return render(request, "remote_clocking_page.html")
    
@login_required()
def remote_clock(request):
    if request.method == "POST":
        user = request.user
        remote_todays_date = timezone.now()
        remote_clock_for_todaysDate_check = RemoteClock.objects.filter(remote_clock_officer_id=user).filter(remote_clocking_date=remote_todays_date)
        if remote_clock_for_todaysDate_check.exists():
            remote_clock_for_today = RemoteClock.objects.get(remote_clock_officer_id=user, remote_clocking_date=remote_todays_date)
            if remote_clock_for_today.remote_number_of_clockings > 0:
                remote_clock_for_today.updateCorrectRemoteClocking(request)
        else:
            remote_clock_for_today = RemoteClock(remote_clock_officer_id=user)
            remote_clock_for_today.updateCorrectRemoteClocking(request)
        remote_clock_for_today.save()
    return redirect("profile") #Bring to view of clock & ok back to profile
    
@login_required()
def manual_clocking(request):
    if request.method == "POST":
        manual_clock_form = ManualClockingForm(request.POST, request.FILES)
        if manual_clock_form.is_valid():
            manual_clock_form.instance.mc_officer_id = request.user
            manual_clock = manual_clock_form.save()
            messages.success(request, 'You have successfully submitted the manual clock form.')
            return redirect(view_manual_clock, manual_clock.pk)
    else:
        manual_clock_form = ManualClockingForm()
    return render(request, 'submit_manual_clocking_form.html', {'manual_clock_form': manual_clock_form})
    
@login_required()
def view_manual_clock(request, pk):
    manual_clock = get_object_or_404(ManualClocking, pk=pk)
    manual_clock.save()
    accept_reject_manual_clock_form = ManualClockAcceptRejectForm()
    
    return render(request, "view_manual_clock.html", {'manual_clock': manual_clock, 'accept_reject_manual_clock_form': accept_reject_manual_clock_form})

@login_required()
def view_submitted_manual_clockings(request):
    submitted_manual_clockings = ManualClocking.objects.filter(checked_by_validator=False)
    return render(request, "view_submitted_manual_clockings.html", {'submitted_manual_clockings': submitted_manual_clockings})
    
@login_required()
def accept_manual_clock(request, pk):
    manual_clock = ManualClocking.objects.get(pk=pk)
    manual_clock.accept_reject_clock = True
    manual_clock.checked_by_validator = True
    manual_clock.validator_id = request.user
    manual_clock.save()
    #cnc = Create New Clock
    #cnc_off_id = manual_clock.mc_officer_id
    #cnc_clocking_date = manual_clock.clocking_date
    
    add_clock = Clocking(officer_id=manual_clock.mc_officer_id, number_of_clockings=4,
                            clocking_in_time=manual_clock.clocking_in_time,
                            clocking_out_time=manual_clock.clocking_out_time,
                            lunch_out_time=manual_clock.lunch_out_time,
                            lunch_in_time=manual_clock.lunch_in_time,
                            clocking_date=manual_clock.clocking_date)
    add_clock.save()
    messages.success(request, 'You have checked and accepted this manual clocking submission.')
    return redirect('view_manual_clock', pk)
    
@login_required()
def reject_manual_clock(request, pk):
    manual_clock = ManualClocking.objects.get(pk=pk)
    manual_clock.accept_reject_clock = False
    manual_clock.checked_by_validator = True
    manual_clock.validator_id = request.user
    manual_clock.save()
    
    messages.success(request, 'You have checked and rejected this manual clocking submission.')
    return redirect('view_manual_clock', pk)

@login_required()    
def accept_reject_manual_clock(request, pk):
    if request.method == "POST":
        accept_reject_manual_clock_form = ManualClockAcceptRejectForm(request.POST, request.FILES)
        if accept_reject_manual_clock_form.is_valid():
            accept_reject_manual_clock_form.instance.mc_officer_id = pk
            manual_clock = accept_reject_manual_clock_form.save()
            manual_clock = ManualClocking.objects.get(pk=pk)
            manual_clock.checked_by_validator = True
            manual_clock.validator_id = request.user
            manual_clock.save()
            if manual_clock.accept_reject_clock == True:
                add_clock = Clocking(officer_id=manual_clock.mc_officer_id, number_of_clockings=4,
                            clocking_in_time=manual_clock.clocking_in_time,
                            clocking_out_time=manual_clock.clocking_out_time,
                            lunch_out_time=manual_clock.lunch_out_time,
                            lunch_in_time=manual_clock.lunch_in_time,
                            clocking_date=manual_clock.clocking_date)
                add_clock.save()
                messages.success(request, 'You have checked and accepted this manual clocking submission.')
            else:
                manual_clock.accept_reject_clock == False
                messages.error(request, 'You have checked and rejected this manual clocking submission.')
        return redirect(view_manual_clock, manual_clock.pk)
            