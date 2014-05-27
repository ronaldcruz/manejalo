# -*- coding: utf-8 -*-
from django.db import models

class Pais(models.Model):

    nombre = models.CharField(max_length=200)
    sigla = models.CharField(max_length=200)

    def __unicode__(self):
        return self.nombre    
    
    
class Ciudad(models.Model):
    nombre = models.CharField(max_length=200)

    def __unicode__(self):
        return self.nombre    
    
    
class Comuna(models.Model):

    ciudad = models.ForeignKey(Ciudad)
    nombre = models.CharField(max_length=200)


    def __unicode__(self):
        return self.nombre    

