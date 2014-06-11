# -*- coding: utf-8 -*-
from django.db import models
from demografia.models import Comuna
#from django_boto.s3.storage import S3Storage

from anuncio.constants import DIRECCION_CHOICES, TRANSMISION_CHOICES, TIPO_VEHICULO_CHOICES
#s3 = S3Storage()

class Tipo(models.Model):
    nombre = models.CharField(max_length=200)

    def __unicode__(self):
        return self.nombre

class Marca(models.Model):
    nombre = models.CharField(max_length=200)

    def __unicode__(self):
        return self.nombre


class Modelo(models.Model):
    marca = models.ForeignKey(Marca)
    nombre = models.CharField(max_length=200)


    def __unicode__(self):
        return self.nombre


class Carroceria(models.Model):
    nombre = models.CharField(max_length=200)

    def __unicode__(self):
        return self.nombre

class Anuncio(models.Model):

    marca = models.ForeignKey(Marca)
    modelo = models.ForeignKey(Modelo)
    version = models.CharField(max_length=200)
    anio = models.IntegerField()
    patente = models.CharField(max_length=10, null=True, blank=True)
    tipo_vehiculo = models.ForeignKey(Tipo)
    carroceria = models.ForeignKey(Carroceria)
    kilometraje = models.IntegerField()
    cilindrada = models.CharField(max_length=100, null=True, blank=True)
    color = models.CharField(max_length=50)
    precio = models.IntegerField()
    conversable = models.BooleanField(default=False)

    comentario = models.TextField(null=True, blank=True)

    potencia = models.CharField(max_length=100, null=True, blank=True)
    motor = models.CharField(max_length=100, null=True, blank=True)
    direccion = models.CharField(max_length=100, null=True, blank=True, choices=DIRECCION_CHOICES)
    transmision = models.CharField(max_length=100, null=True, blank=True, choices=TRANSMISION_CHOICES)

    #Se utilizaran prefijos para poder agrupar los campos al desplegar 
    #el formulario

    # = general
    es_taxi = models.BooleanField(default=False)
    unico_duenio = models.BooleanField(default=False, verbose_name=u'Unico Dueño')

    # = confort  
    aire_acondicionado = models.BooleanField(default=False)
    vidrios_delanteros_elec = models.BooleanField(default=False)
    vidrios_traseros_elec = models.BooleanField(default=False)
    apertura_remota_maleta = models.BooleanField(default=False)
    asiento_conductor_regulable = models.BooleanField(default=False)
    asiento_traseros_abatible = models.BooleanField(default=False)
    cierre_centralizado = models.BooleanField(default=False)
    cierre_centralizado_mando = models.BooleanField(default=False)
    velocidad_crucero = models.BooleanField(default=False)
    espejos_exteriores_elec = models.BooleanField(default=False)
    espejos_exteriores_abatibles_elec = models.BooleanField(default=False)

    #s_ = seguridad

    airbag_conductor = models.BooleanField(default=False)
    airbag_copiloto = models.BooleanField(default=False)
    airbag_traseros = models.BooleanField(default=False)
    alarma = models.BooleanField(default=False)
    doble_traccion = models.BooleanField(default=False)
    frenos_abs = models.BooleanField(default=False)
    inmovilizador_motor = models.BooleanField(default=False)
    neblineros_delanteros = models.BooleanField(default=False)
    neblineros_traseros = models.BooleanField(default=False)
    vidrios_lamina_seguridad = models.BooleanField(default=False)
    
    #e_ = exterior
    luces_xenon = models.BooleanField(default=False)
    barra_portamaletas = models.BooleanField(default=False)
    portamaleta = models.BooleanField(default=False)
    
    #m_ = multimedia
    radio = models.BooleanField(default=False)
    radio_bluetooth = models.BooleanField(default=False)
    radio_auxiliar = models.BooleanField(default=False)
    radio_usb = models.BooleanField(default=False)
    radio_cd = models.BooleanField(default=False)
    radio_dvd = models.BooleanField(default=False)
    radio_pantalla = models.BooleanField(default=False)
    radio_mp3 = models.BooleanField(default=False)
    radio_sd = models.BooleanField(default=False)
    radio_funciones_volante = models.BooleanField(default=False)
    gps = models.BooleanField(default=False)
    
    destacado = models.BooleanField(default=False)
    comuna = models.ForeignKey(Comuna)
    
    imagen = models.ImageField(upload_to='anuncios', blank=True)
    imagen1 = models.ImageField(upload_to='anuncios', blank=True)
    imagen2 = models.ImageField(upload_to='anuncios', blank=True)
    imagen3 = models.ImageField(upload_to='anuncios', blank=True)
    imagen4 = models.ImageField(upload_to='anuncios', blank=True)
    imagen5 = models.ImageField(upload_to='anuncios', blank=True)
    imagen6 = models.ImageField(upload_to='anuncios', blank=True)
    imagen7 = models.ImageField(upload_to='anuncios', blank=True)
    imagen8 = models.ImageField(upload_to='anuncios', blank=True)
    imagen9 = models.ImageField(upload_to='anuncios', blank=True)

    def admin_imagen(self):
        if self.imagen:
            return u'<img width="192" height="144" src="%s" />' % (self.imagen)
        return u'&nbsp'

    admin_imagen.short_description = 'Vista Previa'
    admin_imagen.allow_tags = True


    