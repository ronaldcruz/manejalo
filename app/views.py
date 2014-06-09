from django.shortcuts import render
from anuncio.models import Anuncio
from anuncio.forms import AnuncioForm


def home(request):
	return render(request, 'home.html', {})

def demo(request):
    form = AnuncioForm()
    return render(request, 'demo.html', {'form': form})

