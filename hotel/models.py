from django.db import models

# Create your models here.

class City(models.Model):
    city_code = models.CharField(max_length=5, primary_key=True)
    city_name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "cities"

    def __str__(self):
        return self.city_name

class Hotel(models.Model):
    hotel_name = models.CharField(max_length=200)
    hotel_code = models.CharField(max_length=200)
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    def __str__(self):
        return self.hotel_name