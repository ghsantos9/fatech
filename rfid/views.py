from rfid.models import rfidLogs,Dispositivos

from django.shortcuts import render
from django.template import loader
# Create your views here.

from django.http import HttpResponse

from django.utils import timezone

from django.http import Http404


def index(request):
    #https://docs.djangoproject.com/en/3.1/topics/forms/
    # if request.method == 'POST':
    #     # create a form instance and populate it with data from the request:
    #     print("recebi o post")
    #     print(request.POST)
    #     print(request.POST.get("rfid"))
    id_rfid = request.GET.get('card_uid','',)
    device_token = request.GET.get('device_token','',)

    try:
        chegado = Dispositivos.objects.get(nodeId=device_token)
        print(chegado)
        print("Id do cartão:", id_rfid)
        print("Token do dispositivo:",device_token)
        rfidLogs(rfid=id_rfid,date=timezone.now()).save()
    except Dispositivos.DoesNotExist:
        raise Http404("Dispositivo não cadastrado!")
    return render(request,'rfid/index.html')

    # try:
    #     if Dispositivos.objects.all().filter(nodeId=chegado.nodeId).exists():
    #         print("Id do cartão:", id_rfid)
    #         print("Token do dispositivo:",device_token)
    #         rfidLogs(rfid=id_rfid,date=timezone.now()).save()
    #         return render(request,'rfid/index.html')
    # except Dispositivos.DoesNotExist:
    #     raise Http404("Question does not exist")