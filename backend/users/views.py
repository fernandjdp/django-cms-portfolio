from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
	return render(request, 'users/home.html')

def users(request):
	return render(request, 'users/users.html')

def example(request):
	return render(request, 'users/example.html')