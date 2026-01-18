from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from .forms import ServiceRequestForm,AdminSignUpForm
from django.contrib.auth import login
from django.shortcuts import render

def clients(request):
    context = {
        "title": "Plumber Services",
              "company_name": "Dnick Plumbing Services",
              "email": "info@dnickplumbingservice.com",
              "Address": "123 Kisaasi, Kampala, Uganda",
              "phone_number": "+256 774 587 721" }
    return render(request,"home.html",context)

def about (request):
    context = {
        "title": "Plumber Services",
              "company_name": "Dnick Plumbing Services",
              "email": "info@dnickplumbingservice.com",
              "Address": "123 Kisaasi, Kampala, Uganda",
              "phone_number": "+256 774 587 721" }
    return render(request,"about.html",context)

def service1 (request):
    context = {
        "title": "Plumber Services",
              "company_name": "Dnick Plumbing Services",
              "email": "info@dnickplumbingservice.com",
              "Address": "123 Kisaasi, Kampala, Uganda",
              "phone_number": "+256 774 587 721" }
    return render(request,"plumbing_service.html",context)

def service2 (request):
    context = {
        "title": "Plumber Services",
              "company_name": "Dnick Plumbing Services",
              "email": "info@dnickplumbingservice.com",
              "Address": "123 Kisaasi, Kampala, Uganda",
              "phone_number": "+256 774 587 721" }
    return render(request,"Installation_service.html",context)

def service3 (request):
    context = {
        "title": "Plumber Services",
              "company_name": "Dnick Plumbing Services",
              "email": "info@dnickplumbingservice.com",
              "Address": "123 Kisaasi, Kampala, Uganda",
              "phone_number": "+256 774 587 721" }
    return render(request,"repair_service.html",context)

def contact (request):
    context = {
        "title": "Plumber Services",
              "company_name": "Dnick Plumbing Services",
              "email": "info@dnickplumbingservice.com",
              "Address": "123 Kisaasi, Kampala, Uganda",
              "phone_number": "+256 774 587 721" }
    return render(request,"contact.html",context)


def request_service(request):
    if request.method == 'POST':
      form = ServiceRequestForm(request.POST)
      if form.is_valid():
        form.save()
        return render(request, 'success.html')
    else:
      form = ServiceRequestForm()

    return render(request, 'request_service.html', {'form': form})


def admin_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('admin_dashboard')
    else:
        form = AuthenticationForm(request, data=request.POST)

    return render(request, "admin_login.html", {'form': form})


def admin_signup(request):
    if request.method == "POST":
        form = AdminSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("admin_dashboard")
    else:
        form = AdminSignUpForm(request.POST)

    return render(request, "admin_signup.html", {"form": form})