from django.db import models


class Phone(models.Model):
    phone = models.CharField(max_length=100, null=True)


class Sms(models.Model):
    sms = models.IntegerField()


class Approved(models.Model):
    phone = models.CharField(max_length=100, null=True)
    approved = models.CharField(max_length=10, null=True)
