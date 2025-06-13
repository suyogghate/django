from django.http import HttpResponse
from django.shortcuts import render

def homePage(request):
    return render(request, "index.html")

def aboutUs(request):
    return HttpResponse("Welcome to wscubetech")

def course(request):
    return HttpResponse("<b>We teach python, java, c, c++, etc.</b>")

def courseDetails(request, courseid):
    return HttpResponse(courseid)