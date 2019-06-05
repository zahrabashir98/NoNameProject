# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import Person, Driver, Passenger, Employee, Car, Trip, DPP

admin.site.register(Person)
admin.site.register(Driver)
admin.site.register(Passenger)
admin.site.register(Employee)
admin.site.register(Car)
admin.site.register(Trip)
admin.site.register(DPP)
