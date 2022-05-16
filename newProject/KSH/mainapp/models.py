from django.db import models
from django.shortcuts import render
from django.views import View
import json
from bs4 import BeautifulSoup
import requests
# Create your models here.
from django.db import models

class Note(models.Model):
    title = models.CharField(max_length=255)
    url = models.URLField(max_length=255,default="")
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def ParsingContester(self):
        if Note.url != None:
            responce = requests.get(Note.url)
            soup = BeautifulSoup(responce.text,'lxml')
            quotes = soup.find_all('option')
            for quote in quotes:
                if(quote.text.__contains__("КШ")):
                    print(quote.text[9:])


class Students(models.Model):
    fio = models.CharField(max_length=255)
    class_student = models.IntegerField()
    granted = models.BooleanField(default=False)
    school = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=255)

class Teachers(models.Model):
    fio = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=255)

class Groups(models.Model):
    nameGroup = models.CharField(max_length=255)
    day = models.DateTimeField()
    max_count = models.IntegerField()
    fact_count = models.IntegerField()
    datestart = models.DateTimeField()

class User(models.Model):
    username = models.CharField(max_length= 255)
    email = models.EmailField()
    password = models.CharField(max_length=50)
    admin_root = models.BooleanField(default=False)

