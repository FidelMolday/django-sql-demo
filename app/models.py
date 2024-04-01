#!/usr/bin/env python3


from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=122)
    age = models.IntegerField(null=True)
    location = models.CharField(max_length=12)
    
    