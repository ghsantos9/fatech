from django.shortcuts import render
from django.http import HttpResponse

from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def index(request):
     return render(request,'inicio/index.html')

@login_required
def cadastro(request):
    return render(request,'inicio/cadastro.html')

@login_required
def log(request):
    return render(request,'inicio/log.html')    