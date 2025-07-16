from django.shortcuts import render
from django.http import HttpResponse
from .models import Technonogies

# Create your views here.
def app(request):
    # return render(request, "djangoapp/app.html")
    tech = Technonogies.objects.all()
    return render(request, "djangoapp/app.html", {'data': tech}) 

def app_projects(request):
    # return HttpResponse("OOPs this page is under development")
    return render(request, "djangoapp/projects.html")   