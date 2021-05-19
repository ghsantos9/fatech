from django.db import models

# Create your models here.

class rfidLogs(models.Model):
    rfid = models.CharField(max_length=30)
    date = models.DateTimeField('data registro')

    def __str__(self):
        return self.rfid

class Dispositivos(models.Model):
    nodeId = models.CharField(max_length=30)
    def __str__(self):
        return self.nodeId