import csv
import json
import requests
from django.conf import settings
from .models import City, Hotel

def import_hotel_city_csv():
    """
    Fetches data from a CSV file URL, parses it, and creates City and Hotel objects in the database.

    - This function retrieves CSV data from a specified URL (authenticated with credentials from settings.py).
    - It parses the CSV data and creates City and Hotel objects using Django's `bulk_create` method for efficiency.
    - Error handling is included to catch potential issues during data retrieval or object creation.
    """

    try:
        response = requests.get('http://rachel.maykinmedia.nl/djangocase/city.csv', auth=(settings.USERNAME, settings.PASSWORD))
        if response.status_code == 200:
            #import pdb;pdb.set_trace()
            #print(response.text)# Maps the information in each row to a dict whose keys are given by the optional fieldnames parameter.
            with open("../city.csv", "w") as file:
                file.write(response.text)
            with open("../city.csv", "r") as file:
                reader = csv.reader(file, delimiter=";")
                batch = [row for row in reader]
                bulk = [City(city_code=b[0], city_name=b[1]) for b in batch]
                City.objects.bulk_create(bulk)

            #print(bulk)
        else:
            print(f"Error fetching CSV data: {response.status_code}")
    except Exception as e:
        print(f"Error fetching CSV data: {e}")
    
    try:
        response = requests.get('http://rachel.maykinmedia.nl/djangocase/hotel.csv', auth=(settings.USERNAME, settings.PASSWORD))
        if response.status_code == 200:
            cities = City.objects.all()
            city_lookup = {city.city_code: city for city in cities}
            #import pdb;pdb.set_trace()
            #print(response.text)# Maps the information in each row to a dict whose keys are given by the optional fieldnames parameter.
            with open("../hotel.csv", "w") as file:
                file.write(response.text)
            with open("../hotel.csv", "r") as file:
                reader = csv.reader(file, delimiter=";")
                list_lines = [row for row in reader]
                hotel_batch_data = [
                    Hotel(hotel_name=hotel_name,
                          hotel_code=hotel_code, 
                          city=city_lookup[city_code]) for city_code, hotel_code, hotel_name in list_lines]
                Hotel.objects.bulk_create(hotel_batch_data)
            #print(bulk)
        else:
            print(f"Error fetching CSV data: {response.status_code}")
    except Exception as e:
        print(f"Error fetching CSV data: {e}")
