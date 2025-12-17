from django.shortcuts import render, redirect
from .models import Contato

def index(request):
    return render(
        request,
        'contato/index.html'
    )
def listar(request):
    dados = Contato.objects.all()
    return render(
        request,
        'contato/listar.html',
        {
            'dados':dados
        }
    )
def adicionar(request):
    if request.method == "POST":
        n = request.POST['nome']
        t = request.POST['telefone']
        e = request.POST['email']
        cont = Contato(nome=n, telefone=t, email=e)
        cont.save()
        return redirect('listar')
    return render(
        request,
        'contato/form.html'
    )
def editar(request, numero):
    c = Contato.objects.get(id=numero)
    if request.method == "POST":
        n = request.POST['nome']
        t = request.POST['telefone']
        e = request.POST['email']
        c.nome = n
        c.telefone = t
        c.email = e
        c.save()
        return redirect('listar')
    return render(
        request,
        'contato/edit.html',
        {
            'contato': c
        }
    )
def apagar(request, numero):
    c = Contato.objects.get(id=numero)
    c.delete()
    return redirect('listar')