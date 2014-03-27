#-*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):

    TIPO_USUARIO = (
        ('PAR', 'Particular'),
        ('CON', 'Concesionaria')
    )

    tipo = models.CharField(max_length=10, choices=TIPO_USUARIO, default='PAR')
    