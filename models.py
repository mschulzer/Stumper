from django.db import models
from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist


class Klub(models.Model):
    name = models.CharField(max_length=150)
    addr = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Table(models.Model):
    title = models.CharField(max_length=150)
    price = models.IntegerField(default=800)
    club = models.ForeignKey(Klub, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
