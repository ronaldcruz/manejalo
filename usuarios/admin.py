# -*- coding: utf-8 -*-
from django.contrib import admin
from usuarios.models import Usuario

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'username', 'tipo']
    list_filter = ['tipo']
    fieldsets = (
        (u'Información Personal', {
            'fields': ('first_name', 'last_name', 'email')
        }),
        (u'Configuración', {
            'fields': ('tipo', )
        })
    )


admin.site.register(Usuario, UsuarioAdmin)
