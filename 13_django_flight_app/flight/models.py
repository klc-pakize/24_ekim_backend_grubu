from django.db import models
from django.contrib.auth.models import User

class Flight(models.Model):
    flight_number = models.CharField(max_length=10, unique=True)
    operating_airlines = models.CharField(max_length=30)
    departure_city = models.CharField(max_length=40)
    arrivel_city = models.CharField(max_length = 40)
    date_of_departure = models.DateField()
    estimated_timeof_departure = models.TimeField()

    class Meta:
        verbose_name = "flight"
        verbose_name_plural = "flights"
        
    def __str__(self):
        return f"{self.flight_number} {self.departure_city} {self.arrivel_city}"


class Passenger(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    email = models.EmailField()
    phone_number = models.SmallIntegerField()
    update_date = models.DateTimeField(auto_now=True)
    create_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'passenger'
        verbose_name_plural = 'passengers'

    def _str_(self):
        return f"{self.first_name} - {self.last_name}"
    

class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name = "user_reservation")
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE, related_name = "flight_reservation")
    passenger = models.ManyToManyField(Passenger)