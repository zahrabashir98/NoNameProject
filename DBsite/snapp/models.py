# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Person(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)

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
    


