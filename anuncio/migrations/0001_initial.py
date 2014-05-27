# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Tipo'
        db.create_table(u'anuncio_tipo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'anuncio', ['Tipo'])

        # Adding model 'Marca'
        db.create_table(u'anuncio_marca', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'anuncio', ['Marca'])

        # Adding model 'Modelo'
        db.create_table(u'anuncio_modelo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('marca', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['anuncio.Marca'])),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'anuncio', ['Modelo'])

        # Adding model 'Carroceria'
        db.create_table(u'anuncio_carroceria', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'anuncio', ['Carroceria'])

        # Adding model 'Anuncio'
        db.create_table(u'anuncio_anuncio', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('marca', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['anuncio.Marca'])),
            ('modelo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['anuncio.Modelo'])),
            ('version', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('anio', self.gf('django.db.models.fields.IntegerField')()),
            ('patente', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
            ('tipo_vehiculo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['anuncio.Tipo'])),
            ('carroceria', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['anuncio.Carroceria'])),
            ('kilometraje', self.gf('django.db.models.fields.IntegerField')()),
            ('cilindrada', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('color', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('precio', self.gf('django.db.models.fields.IntegerField')()),
            ('conversable', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('comentario', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('potencia', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('motor', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('direccion', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('transmision', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('aire_acondicionado', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('vidrios_delanteros_elec', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('vidrios_traseros_elec', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('apertura_remota_maleta', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('asiento_conductor_regulable', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('asiento_traseros_abatible', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('cierre_centralizado', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('cierre_centralizado_mando', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('velocidad_crucero', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('espejos_exteriores_elec', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('espejos_exteriores_abatibles_elec', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('airbag_conductor', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('airbag_copiloto', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('airbag_traseros', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('alarma', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('doble_traccion', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('frenos_abs', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('inmovilizador_motor', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('neblineros_delanteros', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('neblineros_traseros', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('vidrios_lamina_seguridad', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('luces_xenon', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('barra_portamaletas', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('portamaleta', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('radio', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('radio_bluetooth', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('radio_auxiliar', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('radio_usb', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('radio_cd', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('radio_dvd', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('radio_pantalla', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('radio_mp3', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('radio_sd', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('radio_funciones_volante', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('gps', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('destacado', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('comuna', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['demografia.Comuna'])),
            ('imagen', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
            ('imagen1', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
            ('imagen2', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
            ('imagen3', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
            ('imagen4', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
            ('imagen5', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
            ('imagen6', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
            ('imagen7', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
            ('imagen8', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
            ('imagen9', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
        ))
        db.send_create_signal(u'anuncio', ['Anuncio'])


    def backwards(self, orm):
        # Deleting model 'Tipo'
        db.delete_table(u'anuncio_tipo')

        # Deleting model 'Marca'
        db.delete_table(u'anuncio_marca')

        # Deleting model 'Modelo'
        db.delete_table(u'anuncio_modelo')

        # Deleting model 'Carroceria'
        db.delete_table(u'anuncio_carroceria')

        # Deleting model 'Anuncio'
        db.delete_table(u'anuncio_anuncio')


    models = {
        u'anuncio.anuncio': {
            'Meta': {'object_name': 'Anuncio'},
            'airbag_conductor': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'airbag_copiloto': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'airbag_traseros': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'aire_acondicionado': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'alarma': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'anio': ('django.db.models.fields.IntegerField', [], {}),
            'apertura_remota_maleta': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'asiento_conductor_regulable': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'asiento_traseros_abatible': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'barra_portamaletas': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'carroceria': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['anuncio.Carroceria']"}),
            'cierre_centralizado': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'cierre_centralizado_mando': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'cilindrada': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'color': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'comentario': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'comuna': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['demografia.Comuna']"}),
            'conversable': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'destacado': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'direccion': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'doble_traccion': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'espejos_exteriores_abatibles_elec': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'espejos_exteriores_elec': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'frenos_abs': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'gps': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imagen': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'imagen1': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'imagen2': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'imagen3': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'imagen4': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'imagen5': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'imagen6': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'imagen7': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'imagen8': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'imagen9': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'inmovilizador_motor': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'kilometraje': ('django.db.models.fields.IntegerField', [], {}),
            'luces_xenon': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'marca': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['anuncio.Marca']"}),
            'modelo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['anuncio.Modelo']"}),
            'motor': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'neblineros_delanteros': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'neblineros_traseros': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'patente': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'portamaleta': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'potencia': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'precio': ('django.db.models.fields.IntegerField', [], {}),
            'radio': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'radio_auxiliar': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'radio_bluetooth': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'radio_cd': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'radio_dvd': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'radio_funciones_volante': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'radio_mp3': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'radio_pantalla': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'radio_sd': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'radio_usb': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'tipo_vehiculo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['anuncio.Tipo']"}),
            'transmision': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'velocidad_crucero': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'version': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'vidrios_delanteros_elec': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'vidrios_lamina_seguridad': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'vidrios_traseros_elec': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'anuncio.carroceria': {
            'Meta': {'object_name': 'Carroceria'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'anuncio.marca': {
            'Meta': {'object_name': 'Marca'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'anuncio.modelo': {
            'Meta': {'object_name': 'Modelo'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'marca': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['anuncio.Marca']"}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'anuncio.tipo': {
            'Meta': {'object_name': 'Tipo'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'demografia.ciudad': {
            'Meta': {'object_name': 'Ciudad'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'demografia.comuna': {
            'Meta': {'object_name': 'Comuna'},
            'ciudad': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['demografia.Ciudad']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['anuncio']