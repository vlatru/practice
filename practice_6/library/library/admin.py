# ~*~ coding: utf-8 ~*~
from django.contrib import admin
from library.models import *


class AuthorsAdmin(admin.ModelAdmin):
    def year(request, self):
        if self.birthyear:
            return self.birthyear
        else:
            return 'возраст неизвестен'

    list_display = ['last_name', 'first_name', 'email', 'year']


class BookImageInline(admin.StackedInline):
    model = BookImage


class BooksAdmin(admin.ModelAdmin):
    def covers(self, obj):
        cur = BookImage.objects.get(id=obj.id)
        return cur.covers_count()

    def cover(self, obj):
        cur = BookImage.objects.get(id=obj.id)
        return cur.cover_tag()

    def large_cover(self, obj):
        cur = BookImage.objects.get(id=obj.id)
        return cur.large_cover_tag()

    cover.allow_tags = True
    large_cover.allow_tags = True

    inlines = [BookImageInline, ]

    list_display = ['title', 'publisher', 'publication_date',
                    'covers', 'cover', 'large_cover']


class PublishersAdmin(admin.ModelAdmin):
    list_display = ['title', 'country', 'city']


class BookImageAdmin(admin.ModelAdmin):
    list_display = ['book_cover', 'cover_tag', 'large_cover_tag']


admin.site.register(Book, BooksAdmin)
admin.site.register(BookImage, BookImageAdmin)
admin.site.register(Author, AuthorsAdmin)
admin.site.register(Publisher, PublishersAdmin)
