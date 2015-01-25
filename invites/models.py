import datetime

from django.db import models

class Person(models.Model):
    def __str__(self):
        strpk = str(self.pk)
        namepk = self.name+strpk
        return namepk
    class Meta:
        verbose_name_plural = 'People'
    name = models.CharField(max_length = 50)
    coming = models.BooleanField(default=False)

class Party(models.Model):
    def __str__(self):
        return str(self.head)
    class Meta:
        verbose_name_plural = 'Parties'
    ID = models.AutoField(primary_key=True)
    head = models.ForeignKey(Person, related_name = '+')
    members = models.ManyToManyField(Person)
    email = models.CharField(max_length=200)
    viewDate = models.DateTimeField(null = True, blank=True)
    submitDate = models.DateTimeField(null = True, blank=True)
    address = models.CharField(max_length=500)
    token = models.CharField(max_length=10)

