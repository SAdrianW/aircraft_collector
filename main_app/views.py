from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Aircraft, Airbase
from .forms import MaintainForm

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
    # list of airbases used
    id_list = aircraft.airbases.all().values_list('id')
    # make list of available airbases by exclude()
    available_airbases = Airbase.objects.exclude(id__in=id_list)
    maintain_form = MaintainForm()
    return render(request, 'aircraft/detail.html', { 
        'aircraft': aircraft, 'maintain_form': maintain_form,
        'airbases': available_airbases
        })

class AircraftCreate(CreateView):
    model = Aircraft
    fields = ['make', 'manufacturer', 'role', 'crew', 'service_years', 'length_m', 'width_m', 'height_m', 'powerplant', 'max_speed_kmh', 'cruise_speed_kmh', 'range_km', 'max_altitude_m', 'capacity' ]

class AircraftUpdate(UpdateView):
    model = Aircraft
    fields = '__all__'

class AircraftDelete(DeleteView):
    model = Aircraft
    success_url = '/aircraft'

def add_maintain(request, aircraft_id):
    form = MaintainForm(request.POST)
    if form.is_valid():
        new_maintain = form.save(commit=False)
        new_maintain.aircraft_id = aircraft_id
        new_maintain.save()
    return redirect('detail', aircraft_id=aircraft_id)

class AirbaseList(ListView):
    model = Airbase

class AirbaseDetail(DetailView):
    model = Airbase

class AirbaseCreate(CreateView):
    model = Airbase
    fields = '__all__'

class AirbaseUpdate(UpdateView):
    model = Airbase
    fields = '__all__'

class AirbaseDelete(DeleteView):
    model = Airbase
    success_url = '/airbases'

def assoc_airbase(request, aircraft_id, airbase_id):
    Aircraft.objects.get(id=aircraft_id).airbases.add(airbase_id)
    return redirect('detail', aircraft_id=aircraft_id)

def remove_airbase(request, aircraft_id, airbase_id):
    Aircraft.objects.get(id=aircraft_id).airbases.remove(airbase_id)
    return redirect('detail', aircraft_id=aircraft_id)
