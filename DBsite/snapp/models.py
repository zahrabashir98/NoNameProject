# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)

    pub_date = models.DateTimeField('date published')
    GENDER = [
    ('Male', 'Male'),
    ('Female', 'Female'),
]

    gender = models.CharField(max_length=6, choices=GENDER)
    id_no = models.AutoField(primary_key=True)
    address = models.CharField(max_length=200)
    # add regex
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return (self.first_name, self.last_name)


class Employee(Person):

    salary = models.IntegerField()
    employee_id = models.IntegerField()
    education = models.CharField(max_length = 20)

    def __str__(self):
        return (self.first_name, self.last_name)


class Driver(Person):

    salary = models.IntegerField()
    driver_id = models.IntegerField()
    education = models.CharField(max_length = 20)
    employee_of_driver = models.ForeignKey('Employee', on_delete=models.CASCADE)

    def __str__(self):
        return (self.first_name, self.last_name)


class Passenger(Person):

    passenger_id = models.IntegerField()
    selected_addresses = models.CharField(max_length = 200)

    def __str__(self):
        return (self.first_name, self.last_name)


class Trip(models.Model):

    trip_id = models.IntegerField()
    selected_addresses = models.CharField(max_length = 200)
    source = models.ForeignKey('Place', on_delete=models.CASCADE)
    car_of_trip = models.ForeignKey('Car', on_delete=models.CASCADE)

    def __str__(self):
        return self.trip_id


class Place(models.Model):

    place_id = models.IntegerField()
    trafficful_hours = models.CharField(max_length = 200)

    def __str__(self):
        return self.place_id


class Car(models.Model):

    plaque = models.AutoField(primary_key=True)
    driver_of_car = models.ForeignKey('Driver', on_delete=models.CASCADE)

    def __str__(self):
        return self.place_id


class Comment(models.Model):

    text = models.CharField(max_length=300)
    passenger_which_comments = models.ForeignKey('Passenger', on_delete=models.CASCADE)
    driver_who_was_commented = models.ForeignKey('Driver', on_delete=models.CASCADE)

    def __str__(self):
        return self.text


class DPP(models.Model):

    passenger_id = models.ForeignKey('Passenger', on_delete=models.CASCADE)
    driver_id = models.ForeignKey('Driver', on_delete=models.CASCADE)
    trip_id = models.ForeignKey('Trip', on_delete=models.CASCADE)


class Destination(models.Model):
    related_trip = models.ForeignKey('Trip', on_delete=models.CASCADE)
    related_place = models.ForeignKey('Place', on_delete=models.CASCADE)


