from django.conf.urls import *
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from library.views import *
from library import settings
from django.contrib.auth.views import *

urlpatterns = patterns(
    '',
    url(r'^login/$', login),
    url(r'^logout/$', logout),
    url(r'^register/$', register),
    url(r'^library/$', BookListView.as_view()),
    url(r'^library/books/$', BookListView.as_view()),
    url(
        r'^library/books/(?P<pk>\d+)/$',
        BookCardView.as_view(), name='book_id'),
    url(r'^library/authors/$', AuthorsListView.as_view()),
    url(
        r'^library/authors/(?P<pk>\d+)/$',
        AuthorCardView.as_view(), name='author_id'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT, }),
)
