from django.shortcuts import render

from .models import Aircraft

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def aircraft_index(request):
    aircraft_list = Aircraft.objects.all()
    return render(request, 'aircraft/index.html', {
        'aircraft_list': aircraft_list
    })

def aircraft_detail(request, aircraft_id):
    aircraft = Aircraft.objects.get(id=aircraft_id)
    return render(request, 'aircraft/detail.html', { 'aircraft': aircraft })