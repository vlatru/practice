from django.conf.urls import patterns, include, url
# from pages import views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'pages.views.home', name='home'),
    url(r'^pages/[0-9]*/$', 'pages.views.home', name='home'),
    url(r'^(?P<param>.*)$', 'pages.views.listing'),
    # url(r'^control_panel/', include('control_panel.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
