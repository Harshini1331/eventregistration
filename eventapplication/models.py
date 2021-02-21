from django.db import models

# Create your models here.
from django.contrib import admin
class Participant(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    phonenumber=models.CharField(max_length=50)
    schoolname=models.CharField(max_length=50)

class ParticipantAdmin(admin.ModelAdmin):
    list_display=("name","email","phonenumber","schoolname")
     