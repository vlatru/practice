# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Book.created'
        db.add_column('library_book', 'created',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 11, 14, 0, 0), auto_now_add=True, db_index=True, blank=True),
                      keep_default=False)

        # Adding field 'Book.updated'
        db.add_column('library_book', 'updated',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 11, 14, 0, 0), auto_now=True, db_index=True, blank=True),
                      keep_default=False)

        # Adding field 'BookImage.created'
        db.add_column('library_bookimage', 'created',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 11, 14, 0, 0), auto_now_add=True, db_index=True, blank=True),
                      keep_default=False)

        # Adding field 'BookImage.updated'
        db.add_column('library_bookimage', 'updated',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 11, 14, 0, 0), auto_now=True, db_index=True, blank=True),
                      keep_default=False)

        # Adding field 'Publisher.created'
        db.add_column('library_publisher', 'created',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 11, 14, 0, 0), auto_now_add=True, db_index=True, blank=True),
                      keep_default=False)

        # Adding field 'Publisher.updated'
        db.add_column('library_publisher', 'updated',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 11, 14, 0, 0), auto_now=True, db_index=True, blank=True),
                      keep_default=False)

        # Adding field 'Author.created'
        db.add_column('library_author', 'created',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 11, 14, 0, 0), auto_now_add=True, db_index=True, blank=True),
                      keep_default=False)

        # Adding field 'Author.updated'
        db.add_column('library_author', 'updated',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 11, 14, 0, 0), auto_now=True, db_index=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Book.created'
        db.delete_column('library_book', 'created')

        # Deleting field 'Book.updated'
        db.delete_column('library_book', 'updated')

        # Deleting field 'BookImage.created'
        db.delete_column('library_bookimage', 'created')

        # Deleting field 'BookImage.updated'
        db.delete_column('library_bookimage', 'updated')

        # Deleting field 'Publisher.created'
        db.delete_column('library_publisher', 'created')

        # Deleting field 'Publisher.updated'
        db.delete_column('library_publisher', 'updated')

        # Deleting field 'Author.created'
        db.delete_column('library_author', 'created')

        # Deleting field 'Author.updated'
        db.delete_column('library_author', 'updated')


    models = {
        'library.author': {
            'Meta': {'object_name': 'Author'},
            'birthyear': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 11, 14, 0, 0)', 'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 11, 14, 0, 0)', 'auto_now': 'True', 'db_index': 'True', 'blank': 'True'})
        },
        'library.book': {
            'Meta': {'object_name': 'Book'},
            'authors': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['library.Author']", 'symmetrical': 'False'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 11, 14, 0, 0)', 'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'publication_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2013, 11, 14, 0, 0)'}),
            'publisher': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['library.Publisher']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 11, 14, 0, 0)', 'auto_now': 'True', 'db_index': 'True', 'blank': 'True'})
        },
        'library.bookimage': {
            'Meta': {'object_name': 'BookImage'},
            'book_cover': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['library.Book']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 11, 14, 0, 0)', 'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'large_image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'small_image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 11, 14, 0, 0)', 'auto_now': 'True', 'db_index': 'True', 'blank': 'True'})
        },
        'library.publisher': {
            'Meta': {'object_name': 'Publisher'},
            'address': ('django.db.models.fields.TextField', [], {}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 11, 14, 0, 0)', 'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 11, 14, 0, 0)', 'auto_now': 'True', 'db_index': 'True', 'blank': 'True'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '32'})
        }
    }

    complete_apps = ['library']