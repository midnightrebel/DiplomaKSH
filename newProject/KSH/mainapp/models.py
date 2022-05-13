from django.db import models
from django.shortcuts import render
from django.views import View
import json
# Create your models here.

from django.db import models
class Note(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)