from django.shortcuts import render

def index(request):

    receitas = {
        1:'Carbonara',
        2:'Bolo de cenoura',
        3:'Sorvete',
        4:'Nutella',
    }
    dados = {
        'receitas': receitas
    }
    return render(request, 'index.html', dados)

def receita(request):
    return render(request, 'receita.html')
