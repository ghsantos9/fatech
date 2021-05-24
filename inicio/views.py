from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from django.contrib.auth.decorators import login_required

from rfid.models import rfidLogs, rfidUsuarios

from django.utils import timezone

# Create your views here.

@login_required
def index(request):
     return render(request,'inicio/index.html')

@login_required
def cadastro(request):
    template = loader.get_template('inicio/cadastro.html')
    registrados = rfidUsuarios.objects.all()
    agora = timezone.now()
    context = {
        'agora': agora,
        'registrados': registrados,
    }
    if request.POST:
        print(request.POST["nome"],request.POST["rfid"],request.POST["email"])
        novo = rfidUsuarios(nome=request.POST["nome"], email=request.POST["email"], rfid=request.POST["rfid"])
        novo.save()
    return HttpResponse(template.render(context, request))

@login_required
def log(request):
    logs_lista = rfidLogs.objects.order_by('date').reverse()[:10]
    #print(usuarios_lista)
    registrados = rfidUsuarios.objects.all()
    lista_registrados=(list(registrados))
    print(lista_registrados)
    agora = timezone.now()
    template = loader.get_template('inicio/log.html')
    
    context = {
        'logs_lista': logs_lista,
        'agora': agora,
        'registrados': registrados,
    }
    return HttpResponse(template.render(context, request))