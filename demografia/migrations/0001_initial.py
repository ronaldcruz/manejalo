# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Pais'
        db.create_table(u'demografia_pais', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('sigla', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'demografia', ['Pais'])

        # Adding model 'Ciudad'
        db.create_table(u'demografia_ciudad', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'demografia', ['Ciudad'])

        # Adding model 'Comuna'
        db.create_table(u'demografia_comuna', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('ciudad', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['demografia.Ciudad'])),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'demografia', ['Comuna'])


    def backwards(self, orm):
        # Deleting model 'Pais'
        db.delete_table(u'demografia_pais')

        # Deleting model 'Ciudad'
        db.delete_table(u'demografia_ciudad')

        # Deleting model 'Comuna'
        db.delete_table(u'demografia_comuna')


    models = {
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
        },
        u'demografia.pais': {
            'Meta': {'object_name': 'Pais'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'sigla': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['demografia']