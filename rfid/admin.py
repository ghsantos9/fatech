from django.contrib import admin
from .models import rfidLogs,Dispositivos, rfidUsuarios

# Register your models here.

admin.site.register(rfidLogs)
admin.site.register(rfidUsuarios)
admin.site.register(Dispositivos)