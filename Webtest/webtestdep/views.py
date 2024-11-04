from django.shortcuts import render
from django.http import HttpResponse

#def index(request):
#      return HttpResponse("<h1>MyClub Event Calendar</h1>")

from django.shortcuts import render

def index(request):
    return render(request,'index.html')