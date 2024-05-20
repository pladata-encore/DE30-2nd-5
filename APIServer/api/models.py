from django.db import models

# Create your models here.


class UserSymptoms(models.Model):
    input_symptoms = models.CharField(max_length=3000)


class RequestDisease(models.Model):
    request_disease = models.CharField(max_length=100)
