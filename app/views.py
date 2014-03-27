from django.shortcuts import render
from anuncio.models import Anuncio


def home(request):
	return render(request, 'home.html', {})


