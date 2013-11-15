# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Customer'
        db.create_table('orders_customer', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, db_index=True, blank=True)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, db_index=True, blank=True)),
            ('firstName', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('lastName', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('address', self.gf('django.db.models.fields.TextField')()),
            ('is_approved', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
        ))
        db.send_create_signal('orders', ['Customer'])

        # Adding model 'Order'
        db.create_table('orders_order', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, db_index=True, blank=True)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, db_index=True, blank=True)),
            ('itemId', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['library.Book'])),
            ('create', self.gf('django.db.models.fields.DateField')(default=datetime.datetime.now)),
            ('customer', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['orders.Customer'], null=True)),
        ))
        db.send_create_signal('orders', ['Order'])


    def backwards(self, orm):
        # Deleting model 'Customer'
        db.delete_table('orders_customer')

        # Deleting model 'Order'
        db.delete_table('orders_order')


    models = {
        'library.author': {
            'Meta': {'object_name': 'Author'},
            'birthyear': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'db_index': 'True', 'blank': 'True'})
        },
        'library.book': {
            'Meta': {'object_name': 'Book'},
            'authors': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['library.Author']", 'symmetrical': 'False'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'publication_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2013, 11, 14, 0, 0)'}),
            'publisher': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['library.Publisher']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'db_index': 'True', 'blank': 'True'})
        },
        'library.publisher': {
            'Meta': {'object_name': 'Publisher'},
            'address': ('django.db.models.fields.TextField', [], {}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'db_index': 'True', 'blank': 'True'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '32'})
        },
        'orders.customer': {
            'Meta': {'object_name': 'Customer'},
            'address': ('django.db.models.fields.TextField', [], {}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'firstName': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_approved': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'lastName': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'db_index': 'True', 'blank': 'True'})
        },
        'orders.order': {
            'Meta': {'object_name': 'Order'},
            'create': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime.now'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'customer': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['orders.Customer']", 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'itemId': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['library.Book']"}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'db_index': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['orders']