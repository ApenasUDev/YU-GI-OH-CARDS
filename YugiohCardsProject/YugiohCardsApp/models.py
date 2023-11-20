from django.db import models

# Create your models here.

class Usuario(models.Model):
    
    nome = models.CharField(max_length=250)
    senha = models.CharField(max_length=25)
class SeusCads(models.Model):
    usuario_cad = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    id_card = models.CharField(max_length=100)

    