from django.contrib import admin
from anuncio.models import Marca, Modelo, Anuncio, Version

class AnuncioAdmin(admin.ModelAdmin):
    list_display = ['marca', 'modelo', 'carroceria', 'kilometraje', 'cilindrada', 'precio', 'tranmision_automatico', 'doble_traccion', 'alarma', 'alzavidrios_electricos', 'aire_acondicionado', 'catalitico', 'cierre_centralizado', 'espejos_electricos', 'espejos_abatibles', 'frenos_abs', 'llantas', 'radio', 'sunroof', 'destacado', 'ciudad', 'admin_imagen']


admin.site.register(Marca)
admin.site.register(Modelo)
admin.site.register(Anuncio)
admin.site.register(Version)
