from django.contrib.postgres.fields import ArrayField
from django.db import models

# Create your models here.
from .enums import ROOM_TYPES


class Owner(models.Model):
    name = models.CharField(max_length=200)
    country_code = models.CharField(max_length=10)
    primary_phone = models.PositiveBigIntegerField()
    email = models.EmailField()
    country_of_residence = models.CharField(max_length=50, null=True, blank=True)
    address = models.TextField(null=True, blank=True)


class HolidayHome(models.Model):
    owners = models.ManyToManyField(Owner, related_name='owners')
    house_pictures = ArrayField(models.URLField(), default=list)
    length = models.PositiveSmallIntegerField()
    width = models.PositiveSmallIntegerField()
    rules = ArrayField(models.CharField(max_length=500), default=list)
    address = models.TextField()
    latitude = models.DecimalField(max_digits=10, decimal_places=7)
    longitude = models.DecimalField(max_digits=10, decimal_places=7)


class HomeDetail(models.Model):
    holiday_home = models.ForeignKey("HolidayHome", on_delete=models.CASCADE)
    rent_for_24_hr_in_rupees = models.PositiveIntegerField()
    date = models.DateField()
    discount = models.PositiveIntegerField(default=0)
    checkout_time = models.TimeField()
    checkin_time = models.TimeField()
    is_booked = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)


class Room(models.Model):
    holiday_home = models.ForeignKey("HolidayHome", on_delete=models.CASCADE)
    room_pictures = ArrayField(models.URLField(), default=list)
    room_type = models.CharField(max_length=50, choices=ROOM_TYPES)
    length = models.PositiveSmallIntegerField()
    width = models.PositiveSmallIntegerField()


