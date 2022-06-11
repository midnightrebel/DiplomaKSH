from django.db import models
from django.views import View
import json
from bs4 import BeautifulSoup
import requests
from django.shortcuts import render



# Create your models here.
from django.db import models
DAYS_OF_WEEK = (
    (0, 'Понедельник'),
    (1, 'Вторник'),
    (2, 'Среда'),
    (3, 'Четверг'),
    (4, 'Пятница'),
    (5, 'Суббота'),
)
AUD_CHOICES = (
    ('306', '306'),
    ('307', '307'),
    ('308', '308'),
    ('309', '309'),
    ('423', '423'),
)





class Teachers(models.Model):
    fio = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=255)
    def __str__(self):
        return self.fio

class Groups(models.Model):
    teacher = models.ForeignKey(Teachers,on_delete=models.CASCADE)
    nameGroup = models.CharField(max_length=255)
    day = models.CharField(choices=DAYS_OF_WEEK, null=True, max_length=255)
    max_count = models.IntegerField()
    fact_count = models.IntegerField()
    aud = models.CharField(max_length=255,choices=AUD_CHOICES,null=True)

    datestart = models.DateTimeField()

    def __str__(self):
        return self.nameGroup

class Students(models.Model):
    first_name = models.CharField(max_length=255)
    second_name = models.CharField(max_length=255)
    third_name = models.CharField(max_length=255)
    group = models.ForeignKey(Groups,on_delete=models.CASCADE)
    class_student = models.IntegerField()
    school = models.CharField(max_length=255)
    subject = models.CharField(max_length=255, default='')
    days = models.CharField(max_length=1, choices=DAYS_OF_WEEK, default='0')
    email = models.EmailField()
    phone_number = models.CharField(max_length=255)
    rating = models.IntegerField()
    done_tasks = models.IntegerField(default=0)
    grant_place = models.BooleanField(default=False)
    def __str__(self):
        return self.fio




