from django.shortcuts import render

def home(request):
    return render(request, 'home_init.html')
