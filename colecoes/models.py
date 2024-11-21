from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Colecao(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    descricao = models.TextField(blank=True)
    colecionador = models.ForeignKey(User, on_delete=models.CASCADE, related_name="colecoes")

    def __str__(self):
        return f"{self.user} - {self.colecionador.username}"