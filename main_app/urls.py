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
    path('aircraft/<int:aircraft_id>/assoc_airbase/<int:airbase_id>/', views.assoc_airbase, name='assoc_airbase'),
    path('aircraft/<int:aircraft_id>/remove_airbase/<int:airbase_id>/', views.remove_airbase, name='remove_airbase'),
    path('airbases/', views.AirbaseList.as_view(), name='airbases_index'),
    path('airbases/<int:pk>/', views.AirbaseDetail.as_view(), name='airbases_detail'),
    path('airbases/create/', views.AirbaseCreate.as_view(), name='airbases_create'),
    path('airbases/<int:pk>/update/', views.AirbaseUpdate.as_view(), name='airbases_update'),
    path('airbases/<int:pk>/delete/', views.AirbaseDelete.as_view(), name='airbases_delete'),
]