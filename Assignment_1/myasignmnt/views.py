from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'myasignmnt/index.html')

def detail(request):
    return render(request, 'myasignmnt/detail.html')