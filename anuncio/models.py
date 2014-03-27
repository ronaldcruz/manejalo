# -*- coding: utf-8 -*-
from django.db import models
from demografia.models import Ciudad
from stdimage.fields import StdImageField
#from django_boto.s3.storage import S3Storage

#s3 = S3Storage()

class Marca(models.Model):
    nombre = models.CharField(max_length=200)

    def __unicode__(self):
        return self.nombre


class Modelo(models.Model):
    marca = models.ForeignKey(Marca)
    nombre = models.CharField(max_length=200)


    def __unicode__(self):
        return self.nombre
        

class Version(models.Model):
    modelo = models.ForeignKey(Modelo)
    nombre = models.CharField(max_length=200)

    def __unicode__(self):
        return self.nombre



class Anuncio(models.Model):

    marca = models.ForeignKey(Marca)
    modelo = models.ForeignKey(Modelo)
    version = models.CharField(max_length=200)
    anio = models.IntegerField()
    patente = models.CharField(max_length=10, null=True, blank=True)
    tipo_vehiculo = models.CharField(max_length=100, null=True, blank=True)
    carroceria = models.CharField(max_length=100, null=True, blank=True)
    kilometraje = models.IntegerField()
    cilindrada = models.CharField(max_length=100)
    color = models.CharField(max_length=50)
    precio = models.IntegerField()


    #Se utilizaran prefijos para poder agrupar los campos al desplegar 
    #el formulario

    #c_ = confort  
    c_aire_acondicionado = models.BooleanField(default=False)
    c_vidrios_delanteros_elec = models.BooleanField(default=False)
    c_vidrios_traseros_elec = models.BooleanField(default=False)
    c_apertura_remota_maleta = models.BooleanField(default=False)
    c_asiento_conductor_regulable = models.BooleanField(default=False)
    c_asiento_traseros_abatible = models.BooleanField(default=False)
    c_cierre_centralizado = models.BooleanField(default=False)
    c_cierre_centralizado_mando = models.BooleanField(default=False)
    c_velocidad_crucero = models.BooleanField(default=False)
    c_espejos_exteriores_elec = models.BooleanField(default=False)
    c_espejos_exteriores_abatibles_elec = models.BooleanField(default=False)

    #s_ = seguridad

    s_airbag_conductor = models.BooleanField(default=False)
    s_airbag_copiloto = models.BooleanField(default=False)
    s_airbag_traseros = models.BooleanField(default=False)
    s_alarma = models.BooleanField(default=False)
    s_doble_traccion = models.BooleanField(default=False)
    s_frenos_abs = models.BooleanField(default=False)
    s_inmovilizador_motor = models.BooleanField(default=False)
    s_neblineros_delanteros = models.BooleanField(default=False)
    s_neblineros_traseros = models.BooleanField(default=False)
    s_vidrios_lamina_seguridad = models.BooleanField(default=False)
    
    #e_ = exterior
    e_luces_xenon = models.BooleanField(default=False)
    e_barra_portamaletas = models.BooleanField(default=False)
    e_portamaleta = models.BooleanField(default=False)
    
    #m_ = multimedia
    m_radio = models.BooleanField(default=False)
    m_radio_bluetooth = models.BooleanField(default=False)
    m_radio_auxiliar = models.BooleanField(default=False)
    m_radio_usb = models.BooleanField(default=False)
    m_radio_cd = models.BooleanField(default=False)
    m_radio_dvd = models.BooleanField(default=False)
    m_radio_pantalla = models.BooleanField(default=False)
    m_radio_mp3 = models.BooleanField(default=False)
    m_radio_sd = models.BooleanField(default=False)
    m_radio_funciones_volante = models.BooleanField(default=False)
    m_gps = models.BooleanField(default=False)
    
    destacado = models.BooleanField(default=False)
    ciudad = models.ForeignKey(Ciudad)
    
    #imagen = StdImageField(upload_to='anuncios', blank=True, variations={'large': (640, 480, True), 'thumbnail': (125, 100, True)})
    #imagen1 = StdImageField(upload_to='anuncios', blank=True, variations={'large': (640, 480, True), 'thumbnail': (125, 100, True)})
    #imagen2 = StdImageField(upload_to='anuncios', blank=True, variations={'large': (640, 480, True), 'thumbnail': (125, 100, True)})
    #imagen3 = StdImageField(upload_to='anuncios', blank=True, variations={'large': (640, 480, True), 'thumbnail': (125, 100, True)})
    #imagen4 = StdImageField(upload_to='anuncios', blank=True, variations={'large': (640, 480, True), 'thumbnail': (125, 100, True)})
    #imagen5 = StdImageField(upload_to='anuncios', blank=True, variations={'large': (640, 480, True), 'thumbnail': (125, 100, True)})
    #imagen6 = StdImageField(upload_to='anuncios', blank=True, variations={'large': (640, 480, True), 'thumbnail': (125, 100, True)})
    #imagen7 = StdImageField(upload_to='anuncios', blank=True, variations={'large': (640, 480, True), 'thumbnail': (125, 100, True)})
    #imagen8 = StdImageField(upload_to='anuncios', blank=True, variations={'large': (640, 480, True), 'thumbnail': (125, 100, True)})
    #imagen9 = StdImageField(upload_to='anuncios', blank=True, variations={'large': (640, 480, True), 'thumbnail': (125, 100, True)})

    imagen = models.ImageField(upload_to='anuncios')
    

    def admin_imagen(self):
        if self.imagen:
            return u'<img width="192" height="144" src="%s" />' % (self.imagen.thumbnail.url)
        return u'&nbsp'

    admin_imagen.short_description = 'Vista Previa'
    admin_imagen.allow_tags = True

