# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Author'
        db.create_table('library_author', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75, null=True)),
        ))
        db.send_create_signal('library', ['Author'])

        # Adding model 'Book'
        db.create_table('library_book', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('publisher', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['library.Publisher'])),
            ('publication_date', self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2013, 11, 13, 0, 0))),
        ))
        db.send_create_signal('library', ['Book'])

        # Adding M2M table for field authors on 'Book'
        m2m_table_name = db.shorten_name('library_book_authors')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('book', models.ForeignKey(orm['library.book'], null=False)),
            ('author', models.ForeignKey(orm['library.author'], null=False))
        ))
        db.create_unique(m2m_table_name, ['book_id', 'author_id'])

        # Adding model 'Publisher'
        db.create_table('library_publisher', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('address', self.gf('django.db.models.fields.TextField')()),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('country', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('website', self.gf('django.db.models.fields.URLField')(max_length=32)),
        ))
        db.send_create_signal('library', ['Publisher'])

        # Adding model 'BookImage'
        db.create_table('library_bookimage', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('small_image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('large_image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('book_cover', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['library.Book'])),
        ))
        db.send_create_signal('library', ['BookImage'])


    def backwards(self, orm):
        # Deleting model 'Author'
        db.delete_table('library_author')

        # Deleting model 'Book'
        db.delete_table('library_book')

        # Removing M2M table for field authors on 'Book'
        db.delete_table(db.shorten_name('library_book_authors'))

        # Deleting model 'Publisher'
        db.delete_table('library_publisher')

        # Deleting model 'BookImage'
        db.delete_table('library_bookimage')


    models = {
        'library.author': {
            'Meta': {'object_name': 'Author'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '32'})
        },
        'library.book': {
            'Meta': {'object_name': 'Book'},
            'authors': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['library.Author']", 'symmetrical': 'False'}),
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