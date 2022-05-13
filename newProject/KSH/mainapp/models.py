from django.db import models
from django.shortcuts import render
from django.views import View
import json
# Create your models here.
import parsing
from django.db import models
class Note(models.Model):
    title = models.CharField(max_length=255)
    url = models.URLField(max_length=255,default="")
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    def ParsingContester(self,request):
        if Note.url != None:
            parsing.parsingVt(Note.url)


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


