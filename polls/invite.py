import datetime

from django.db import models
from django.utils import timezone

class Party(models.Model):
    def __str__(self):
        return self.ID
    ID = models.PrimaryKey(PrimaryKey=True)
    Email = models.CharField(max_length=200)
    ViewDate = models.DateTimeField(auto_now = True)
    SubmitDate = models.DateTimeField(auto_now = True)
    Address = models.CharField(max_length=500)
    Token = models.CharField(max_length=10)

class Person(models.Model):
    def __str__(self):
        return self.Name
    Name = models.CharField(max_length = 50)
    Party = models.ForeignKey(ID)
    Coming = models.BooleanField(default=False)