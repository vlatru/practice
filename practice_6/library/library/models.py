from django.db import models
from utils.models import TimeStampedModel

# Create your models here.
import os
import datetime
from library.settings import MEDIA_ROOT, MEDIA_URL


class Author(TimeStampedModel):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    email = models.EmailField(null=True)
    birthyear = models.IntegerField('Birth Year', null=True)

    def get_absolute_url(self):
        return "/library/authors/%s/" % self.id

    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)


class Book(TimeStampedModel):
    title = models.CharField(max_length=128)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey('Publisher')
    publication_date = models.DateField(default=datetime.datetime.now())
    description = models.TextField('Description', default='')

    def get_absolute_url(self):
        return "/library/books/%s/" % self.id

    def __unicode__(self):
        return self.title


class Publisher(TimeStampedModel):
    title = models.CharField(max_length=32)
    address = models.TextField()
    city = models.CharField(max_length=64)
    country = models.CharField(max_length=64)
    website = models.URLField(max_length=32)

    def __unicode__(self):
        #return u'%s (%s)'%(self.title, self.website)
        return u'%s (%s, %s)' % (self.title, self.city, self.country)


class BookImage(TimeStampedModel):
    small_image = models.ImageField(upload_to=MEDIA_ROOT)
    large_image = models.ImageField(
        blank=True, null=True, upload_to=MEDIA_ROOT)
    book_cover = models.ForeignKey('Book')

    def __unicode__(self):
        return "%s" % self.id

    def covers_count(self):
        i = 0
        if self.small_image:
            i += 1
        if self.large_image:
            i += 1
        return i

    def cover_tag(self):
        return '<img src="%s%s"/>' % (
            MEDIA_URL, os.path.basename(self.small_image.name))

    def large_cover_tag(self):
        return '<img src="%s%s"/>' % (
            MEDIA_URL, os.path.basename(self.large_image.name))

    cover_tag.allow_tags = True
    large_cover_tag.allow_tags = True
