# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'DataScraping'
        db.create_table(u'app_datascraping', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('marca', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('modelo', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('version', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('anio', self.gf('django.db.models.fields.IntegerField')()),
            ('patente', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('tipo_vehiculo', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('carroceria', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('color', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('kilometraje', self.gf('django.db.models.fields.IntegerField')()),
            ('cilindrada', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('transmision', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('direccion', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('aire', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('radio', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('alzavidrios', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('espejos', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('frenos', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('airbag', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('cierre', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('combustible', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('traccion', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('llantas', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('puertas', self.gf('django.db.models.fields.IntegerField')()),
            ('alarma', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('techo', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('contacto', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('ubicacion', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('telefonos', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('comuna', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('ciudad', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('imagenes', self.gf('django.db.models.fields.CharField')(max_length=9000)),
            ('precio', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'app', ['DataScraping'])


    def backwards(self, orm):
        # Deleting model 'DataScraping'
        db.delete_table(u'app_datascraping')


    models = {
        u'app.datascraping': {
            'Meta': {'object_name': 'DataScraping'},
            'airbag': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'aire': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'alarma': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'alzavidrios': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'anio': ('django.db.models.fields.IntegerField', [], {}),
            'carroceria': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'cierre': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'cilindrada': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'ciudad': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'color': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'combustible': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'comuna': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'contacto': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'direccion': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'espejos': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'frenos': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imagenes': ('django.db.models.fields.CharField', [], {'max_length': '9000'}),
            'kilometraje': ('django.db.models.fields.IntegerField', [], {}),
            'llantas': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'marca': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'modelo': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'patente': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'precio': ('django.db.models.fields.IntegerField', [], {}),
            'puertas': ('django.db.models.fields.IntegerField', [], {}),
            'radio': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'techo': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'telefonos': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'tipo_vehiculo': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'traccion': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'transmision': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'ubicacion': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'version': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['app']