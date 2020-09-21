from django.shortcuts import render, redirect, HttpResponseRedirect, get_object_or_404, reverse

# Create your views here.
def landing_page(request):
    return render(request, "landing_page.html")
    
