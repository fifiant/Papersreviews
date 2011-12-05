from django.conf.urls.defaults import patterns, include, url
import os
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
site_media = os.path.join(os.path.dirname(__file__), 'site_media')
urlpatterns = patterns('',
    #Site media
    (r'^site_media/(?P<path>.*)$', 'django.views.static.serve',{'document_root': site_media}),
    # Papers URLS Management
    url(r'^$', include('Papersreviews.papers.urls')),
    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
)
