from django.db import models
import random
import string

class Person(models.Model):
    def __str__(self):
        strpk = str(self.pk)
        namepk = self.name+strpk
        return namepk
    class Meta:
        verbose_name_plural = 'People'
    name = models.CharField(max_length = 50)
    coming = models.NullBooleanField(default=None)

def tokengenerator():
    return ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(7))

class Party(models.Model):
    def __str__(self):
        return str(self.head)
    class Meta:
        verbose_name_plural = 'Parties'
    ID = models.AutoField(primary_key=True)
    head = models.ForeignKey(Person, related_name = '+')
    members = models.ManyToManyField(Person)
    email = models.CharField(max_length=200)
    emailInvite = models.BooleanField(default=True)
    viewDate = models.DateTimeField(null = True, blank=True, default=None)
    submitDate = models.DateTimeField(null = True, blank=True, default=None)
    address = models.TextField(default=None)
    token = models.CharField(max_length = 7, default=tokengenerator, blank=True, unique=True)
