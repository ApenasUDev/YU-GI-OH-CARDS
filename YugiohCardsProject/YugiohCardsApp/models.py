from django.db import models

# Create your models here.

class Usuario(models.Model):
    nome = models.CharField(max_length=250)
    senha = models.CharField(max_length=25)
class SeusCads(models.Model):
    id_card = models.CharField(max_length=100)

    