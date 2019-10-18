from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def homepage(request):
	return HttpResponse('Hello World, I am a Django application. Created by Anil')

