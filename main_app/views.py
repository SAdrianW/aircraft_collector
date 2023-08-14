from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Aircraft
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
    maintain_form = MaintainForm()
    return render(request, 'aircraft/detail.html', { 
        'aircraft': aircraft, 'maintain_form': maintain_form
        })

class AircraftCreate(CreateView):
    model = Aircraft
    fields = '__all__'

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
