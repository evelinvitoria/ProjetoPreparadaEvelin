from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    #return HttpResponse('<h1> olá <h1><p>hello world<p>')
    return render(request, 'gallery/index.html')
    
def imagem(request):
    return render(request, 'gallery/imagem.html')

