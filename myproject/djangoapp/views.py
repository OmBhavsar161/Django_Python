from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def app(request):
    return render(request, "djangoapp/app.html")

def app_projects(request):
    # return HttpResponse("OOPs this page is under development")
    return render(request, "djangoapp/projects.html")