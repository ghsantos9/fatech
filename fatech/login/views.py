from django.shortcuts import render
from django.template import loader
# Create your views here.

from django.http import HttpResponse

def index(request):
    if request.method == 'POST':
        print(request.POST['username'],request.POST['password'])
        
    return render(request,'login/index.html')
