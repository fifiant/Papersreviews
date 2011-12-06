from django.conf.urls.defaults import *
from Papersreviews.papers.models import Papers

urlpatterns = patterns('',
    #(r'^/search/', 'Papersreviews.papers.views.search_page'),
    (r'^$', 'Papersreviews.deposer.views.index'),
)