from django.shortcuts import render


import myapp

# Create your views here.
def index(request):
	return render(request,'index.html')

def service(request):
	return render(request,'services.html')

def result(request):
	return render(request,'results.html')

def analytics(request):
	return render(request,'analytics.html')