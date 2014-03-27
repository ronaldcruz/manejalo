from django.contrib import admin
from app.models import DataScraping

class DataScrapingAdmin(admin.ModelAdmin):
    list_display = ['marca', 'modelo', 'version', 'anio', 'precio']

admin.site.register(DataScraping, DataScrapingAdmin)


