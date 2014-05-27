from django.shortcuts import render
from anuncio.models import Anuncio
from anuncio.forms import AnuncioForm

def show(request, anuncio_id):
    anuncio = Anuncio.objects.get(id=anuncio_id)
    return render(request, 'advertisement/advertisement.html', {'anuncio': anuncio})


def create(request):
    form = AnuncioForm()
    return render(request, 'advertisement/submit.html', {'form': form})

