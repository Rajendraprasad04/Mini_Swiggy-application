from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def delivery(request):
    return HttpResponse('<h1><center>Currently there is no any deliveries</center></h1>')
