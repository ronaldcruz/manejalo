from django.core.management.base import BaseCommand, CommandError
from anuncio.models import Anuncio, Marca, Modelo
from app.models import DataScraping
from demografia.models import Ciudad


from django.core.files import File
from django.core.files.temp import NamedTemporaryFile

import datetime
import random
import requests

class Command(BaseCommand):
    
    def handle(self, *args, **options):
        self.stdout.write('Convirtiendo data...')

        avisos = DataScraping.objects.all()[:2]

        for aviso in avisos:

            imagenes = aviso.imagenes.split('###RCC###')
            imagen_portada = imagenes[0]

            r = requests.get(imagen_portada)

            img_temp = NamedTemporaryFile(delete=True)
            img_temp.write(r.content)
            img_temp.flush()

            anu = Anuncio()
            anu.marca, creado = Marca.objects.get_or_create(nombre=aviso.marca)
            anu.modelo, creado = Modelo.objects.get_or_create(nombre=aviso.modelo.replace('. ', '').replace('- ', '').replace('-', '').lstrip('.').lstrip('-').lower().capitalize())
            anu.version = aviso.version
            anu.anio = aviso.anio
            anu.patente = aviso.patente
            anu.tipo_vehiculo = aviso.tipo_vehiculo
            anu.carroceria = aviso.carroceria
            anu.kilometraje = aviso.kilometraje
            anu.cilindrada = aviso.cilindrada
            anu.precio = aviso.precio
            anu.color = aviso.color
            anu.ciudad, creado = Ciudad.objects.get_or_create(nombre=aviso.ciudad)
            anu.save()

            anu.imagen.save("image.jpg", File(img_temp))
            
        self.stdout.write('Successfully closed poll')




    def save_image_from_url(model, url):
        r = requests.get(url)

        img_temp = NamedTemporaryFile(delete=True)
        img_temp.write(r.content)
        img_temp.flush()

        model.image.save("image.jpg", File(img_temp), save=True)