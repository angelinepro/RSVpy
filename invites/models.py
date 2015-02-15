from django.db import models
from random import SystemRandom


TOKEN_CHARSET = '3479ACEFHJKLMNPRTUVWXYabcdefghijkmnopqrstuvwxyz'

class Person(models.Model):
    name = models.CharField(max_length=50)
    coming = models.NullBooleanField(default=None)

    class Meta:
        verbose_name_plural = 'People'

    def __str__(self):
        return self.name


class Party(models.Model):
    ID = models.AutoField(primary_key=True)
    head = models.ForeignKey(Person, related_name='+')
    members = models.ManyToManyField(Person)
    email = models.CharField(max_length=200)
    emailInvite = models.BooleanField(default=True)
    emailSent = models.BooleanField(default=False)
    viewDate = models.DateTimeField(null=True, blank=True, default=None)
    submitDate = models.DateTimeField(null=True, blank=True, default=None)
    address = models.TextField(default=None)
    token = models.CharField(max_length=7, blank=True, unique=True, db_index=True)

    class Meta:
        verbose_name_plural = 'Parties'

    def __str__(self):
        return '%s (party_id=%d)' % (self.head, self.pk)

    def save(self, *args, **kwargs):
        if not self.token:
            self.token = self.random_unique_token()
        super(Party, self).save(*args, **kwargs)

    @classmethod
    def random_unique_token(cls):
        # XXX: Hope it doesn't take too long!!
        while True:
            token = ''.join(SystemRandom().choice(TOKEN_CHARSET) for _ in range(7))
            if not len(cls.objects.filter(token=token)):
                return token


class SeenBrowser(models.Model):
    id = models.AutoField(primary_key=True)
    browser = models.CharField(max_length=255)
    version = models.CharField(max_length=64)
    times = models.PositiveIntegerField(default=0)
