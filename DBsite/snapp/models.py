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

    gender = models.CharField(
        max_length=6,
        choices=GENDER,
        
    )
    id_no = models.AutoField(primary_key=True)
    address = models.CharField(max_length=200, null = True)
    # add regex
    phone_number = models.CharField(max_length=15,  null = True)

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

    def __str__(self):
        return (self.first_name, self.last_name)


class Passenger(Person):

    passenger_id = models.IntegerField()
    selected_addresses = models.CharField(max_length = 200)

    def __str__(self):
        return (self.first_name, self.last_name)