from django.shortcuts import render
from django.template import loader
# Create your views here.

from django.http import HttpResponse


def index(request):
    #https://docs.djangoproject.com/en/3.1/topics/forms/
    # if request.method == 'POST':
    #     # create a form instance and populate it with data from the request:
    #     print("recebi o post")
    #     print(request.POST)
    #     print(request.POST.get("rfid"))
    print("Id do cartão:",request.GET.get('card_uid','',))
    print("Token do dispositivo:",request.GET.get('device_token','',))
    return render(request,'rfid/index.html')
