from django.shortcuts import render

aircraft_list = [
    {'name': 'A-10 Thunderbolt', 'role': 'Close Air Support', 'capacity': 'GUA-8 Avenger Gatling Cannon', 'size': 'L: 16.2m W: 17.5m H: 4.5m'},
    {'name': 'C-17 Globemaster', 'role': 'Transport', 'armament-capacity': '77,519kg cargo', 'size': 'L: 53m W: 51.7m H: 16.8m'}
]

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def aircraft_index(request):
    return render(request, 'aircraft/index.html', {
        'aircraft_list': aircraft_list
    })
