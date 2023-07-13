from django.shortcuts import render
from django.http import HttpResponse
import datetime
from .models import Transacao

def home(request):
    data= {}
    data['now'] = datetime.datetime.now()
    data['osf'] = ['f1','f1','f3']

    #html = "<html><body>It is now %s.</body></html>" % now
    return render(request, 'myhome.html', data)

def teste(request):
    data= {}
    data['now'] = datetime.datetime.now()
    
    return render(request, 'index.html', data)

def listagem(request):
    data = {}
    data['transacao'] = Transacao.objects.all()
    return render(request, 'listagem.html', data)
# Create your views here.
