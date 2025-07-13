from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("This in Django Home Page")
    return render(request, 'index.html')

def about(request):
    return HttpResponse("About Section for learing django coding. Django is framework.")