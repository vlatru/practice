# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Book.description'
        db.add_column('library_book', 'description',
                      self.gf('django.db.models.fields.TextField')(default=''),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Book.description'
        db.delete_column('library_book', 'description')


    models = {
        'library.author': {
            'Meta': {'object_name': 'Author'},
            'birthyear': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '32'})
        },
        'library.book': {
            'Meta': {'object_name': 'Book'},
            'authors': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['library.Author']", 'symmetrical': 'False'}),
            'description': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'publication_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2013, 11, 13, 0, 0)'}),
            'publisher': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['library.Publisher']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        'library.bookimage': {
            'Meta': {'object_name': 'BookImage'},
            'book_cover': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['library.Book']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'large_image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'small_image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'})
        },
        'library.publisher': {
            'Meta': {'object_name': 'Publisher'},
            'address': ('django.db.models.fields.TextField', [], {}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '32'})
        }
    }

    complete_apps = ['library']