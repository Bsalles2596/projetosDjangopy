from django.db import models

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    login = models.TextField(max_length=255)
    senha = models.TextField(max_length=10)
