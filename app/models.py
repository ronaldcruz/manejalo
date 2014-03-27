# -*- coding: utf-8 -*-
from django.db import models

class DataScraping(models.Model):

    marca = models.CharField(max_length=200)
    modelo = models.CharField(max_length=200)
    version = models.CharField(max_length=200)
    anio = models.IntegerField()
    patente = models.CharField(max_length=200)
    tipo_vehiculo = models.CharField(max_length=200)
    carroceria = models.CharField(max_length=200)
    color = models.CharField(max_length=200)
    kilometraje = models.IntegerField()
    cilindrada = models.CharField(max_length=200)
    transmision = models.CharField(max_length=200)
    direccion = models.CharField(max_length=200)
    aire = models.CharField(max_length=200)
    radio = models.CharField(max_length=200)
    alzavidrios = models.CharField(max_length=200)
    espejos = models.CharField(max_length=200)
    frenos = models.CharField(max_length=200)
    airbag = models.CharField(max_length=200)
    cierre = models.CharField(max_length=200)
    combustible = models.CharField(max_length=200)
    traccion = models.CharField(max_length=200)
    llantas = models.CharField(max_length=200)
    puertas = models.IntegerField()
    alarma = models.CharField(max_length=200)
    techo = models.CharField(max_length=200)
    contacto = models.CharField(max_length=200)
    ubicacion = models.CharField(max_length=200)
    telefonos = models.CharField(max_length=200)
    comuna = models.CharField(max_length=200)
    ciudad = models.CharField(max_length=200)

    imagenes = models.CharField(max_length=9000)
    precio = models.IntegerField()
    
    def admin_imagen(self):
        if self.imagenes and self.imagenes != '':
            print self.imagenes
            split_imgs = self.imagenes.split('###RCC###')
            print split_imgs
            if len(split_imgs) > 0:
                imagen = split_imgs[0]
                return u'<img width="192" height="144" src="%s" />' % (imagen)
        
        return u'&nbsp'

    admin_imagen.short_description = 'Vista Previa'
    admin_imagen.allow_tags = True
