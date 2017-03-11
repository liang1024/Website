from django.shortcuts import render

# Create your views here.
from django.http import  HttpResponse

def index(request):
    return HttpResponse("<h1>This is the Music app HomePage</h1>")

def detail(request,albun_id):
    return HttpResponse("<h2>Details for Album id :"+str(albun_id)+"</h2>")