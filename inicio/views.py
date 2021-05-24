from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from django.contrib.auth.decorators import login_required

from rfid.models import rfidLogs
# Create your views here.

@login_required
def index(request):
     return render(request,'inicio/index.html')

@login_required
def cadastro(request):
    return render(request,'inicio/cadastro.html')

@login_required
def log(request):
    usuarios_lista = rfidLogs.objects.order_by('rfid')
    print(usuarios_lista)
    template = loader.get_template('inicio/log.html')
    context = {
        'usuarios_lista': usuarios_lista,
    }
    return HttpResponse(template.render(context, request))