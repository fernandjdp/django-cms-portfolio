from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
	return render(request, 'portfolio/home.html')

def portfolio(request):
	return render(request, 'portfolio/portfolio.html')

def example(request):
	return render(request, 'portfolio/example.html')