from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('aircraft/', views.aircraft_index, name='main_hangar'),
    path('aircraft/<int:aircraft_id>/', views.aircraft_detail, name='detail'),
]