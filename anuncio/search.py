from django.shortcuts import render
from anuncio.models import Anuncio


def search(request):
	anuncios = Anuncio.objects.all().order_by('-destacado')
	return render(request, 'resultados.html', {'anuncios': anuncios})