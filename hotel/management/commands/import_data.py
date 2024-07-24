from django.core.management.base import BaseCommand
from hotel.import_data import import_hotel_city_csv

#Getting credentials from env file
from django.conf import settings

#Django will register a manage.py command for each Python module in that directory whose name doesn’t begin with an underscore.

class Command(BaseCommand):
    help = "Imports csv data from CSV over authenticated HTTP and saves it to a file. Then uses bulk_create to pass data to models"

    def handle(self, *args, **kwargs):
        """
        The actual logic of the command. Subclasses must implement
        this method.
        """

        import_hotel_city_csv()

