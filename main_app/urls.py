from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('aircraft/', views.aircraft_index, name='main_hangar'),
    path('aircraft/<int:aircraft_id>/', views.aircraft_detail, name='detail'),
    path('aircraft/create/', views.AircraftCreate.as_view(), name='aircraft_create'),
    path('aircraft/<int:pk>/update/', views.AircraftUpdate.as_view(), name='aircraft_update'),
    path('aircraft/<int:pk>/delete/', views.AircraftDelete.as_view(), name='aircraft_delete'),
    path('aircraft/<int:aircraft_id>/add_maintain/', views.add_maintain, name='add_maintain'),
]