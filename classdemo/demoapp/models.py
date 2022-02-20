from django.db import models

# Create your models here.


class Hotels(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200, null=False)
    price = models.IntegerField()
    available = models.BooleanField(null=True)

    def __str__(self):
        return self.name


class Guest(models.Model):
    id = models.IntegerField(primary_key=True)
    guest_name = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.guest_name