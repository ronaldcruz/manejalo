from django.shortcuts import render
from anuncio.models import Anuncio

def show(request, anuncio_id):
    anuncio = Anuncio.objects.get(id=anuncio_id)
    return render(request, 'advertisement/advertisement.html', {'anuncio': anuncio})


def create(request):
    return render(request, 'advertisement/submit.html', {})

