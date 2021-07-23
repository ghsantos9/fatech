from django.db import models
from django.db.models.fields import EmailField

# Create your models here.

class rfidLogs(models.Model):
    rfid = models.CharField(max_length=30, blank=False)
    date = models.DateTimeField('data registro')

    def __str__(self):
        return self.rfid

class Dispositivos(models.Model):
    nodeId = models.CharField(max_length=30)
    def __str__(self):
        return self.nodeId

class rfidUsuarios(models.Model):
    nome = models.CharField(max_length=60, blank=False)
    rfid = models.CharField(max_length=30, blank=False)
    email = EmailField(max_length=30, blank=False)

    def __str__(self):
        return f'{self.rfid}'