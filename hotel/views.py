from django.shortcuts import render

from .models import City, Hotel
from hotel.import_data import import_hotel_city_csv
from django.views.generic import ListView, DetailView

# Create your views here.

# Decide using BaseCommands to import data, 
# or writing a view for data import through POST request

def home(request):
    context = {}
    return render(request, "hotel/home.html")

class CityListView(ListView):
    model = City

# why django didnt recognize tmeplate name automatically?
class HotelListView(ListView):
    model = City
    template_name = 'hotel/hotel_list.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        city_code = self.kwargs.get('city_code')
        if city_code:
            context['city'] = City.objects.get(city_code=city_code)
            context['hotels'] = Hotel.objects.filter(city__city_code=city_code)
        return context
