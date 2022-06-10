from django.db import models

# Create your models here.


class Posts(models.Model):
    nome = models.CharField(max_length=50)
    data = models.DateField()
    descricao = models.TextField(max_length=200)
    curtidas = models.BigIntegerField(null=True, blank=True)