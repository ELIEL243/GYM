import datetime

from django.db import models

# Create your models here.


class Client(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=13)
    address = models.TextField()

    def __str__(self):
        return self.name


type_offers = (
    ('normal', 'normal'),
    ('special', 'special'),
)


class Coach(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=13)
    address = models.TextField()
    hire_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Offre(models.Model):
    type = models.CharField(choices=type_offers, max_length=255)
    coach = models.ForeignKey(Coach, on_delete=models.SET_NULL, null=True, blank=True)
    price = models.FloatField()

    def __str__(self):
        return self.type


class Abonnement(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    offer = models.ForeignKey(Offre, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True, null=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)

    @property
    def echeance_date(self):
        echeance = self.date + datetime.timedelta(days=30)
        return str(echeance.date())


class Equipment(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    quantity = models.IntegerField()

    def __str__(self):
        return self.name
