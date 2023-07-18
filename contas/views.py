from django.shortcuts import render, redirect
from django.http import HttpResponse
import datetime
from .models import Transacao
from .form import TransacaoForm

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
    data['transacoes'] = Transacao.objects.all()
    return render(request, 'listagem.html', data)

def nova_transacao(request):
    form = TransacaoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('url_listagem')
    data = {}
    data['form'] = form
    return render(request, 'form.html', data)

def update(request, pk):
    transacao = Transacao.objects.get(pk=pk)
    form = TransacaoForm(request.POST or None, instance=transacao)
    data = {}
    if form.is_valid():
        form.save()
        return redirect('url_listagem')
    data['form'] = form
    data['transacao'] = transacao
    return render(request, 'form.html', data)

def delete(request, pk):
    transacao = Transacao.objects.get(pk=pk)
    transacao.delete()
    return redirect('url_listagem')
# Create your views here.
