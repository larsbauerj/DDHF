# from django.conf.urls.defaults import *
from django.conf.urls import patterns, include, url
# from django.conf import settings
import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

import views

from views import AboutView
from views import ItemsView
from views import display_meta

from models import Producers
from models import Files
from models import Items
from models import Donators
from models import Pictures


urlpatterns = patterns('',
    url(r'^meta/', display_meta),
    url(r'^readonly/about$', AboutView),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', { 'show_indexes':True, 'document_root': settings.MEDIA_ROOT,}),
    # "/home/bauer/DDHF/pictures/", }),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', { 'show_indexes':True, 'document_root': settings.MEDIA_ROOT, }),

    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/', include(admin.site.urls)),
)

