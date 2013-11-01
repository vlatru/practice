from django.conf.urls import patterns
from django.conf.urls import include
from django.conf.urls import url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', 'library.views.home'),
    url(r'^library/$', 'library.views.books'),
    url(r'^library/books/$', 'library.views.books'),
    url(r'^library/books/(\d+)/$', 'library.views.book'),
    url(r'^library/authors/$', 'library.views.authors'),
    url(r'^library/authors/(\d+)/$', 'library.views.author'),
    # url(r'^library/', include('library.foo.urls')),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
