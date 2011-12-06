from django.conf.urls.defaults import *
from Papersreviews.papers.models import Papers

urlpatterns = patterns('',
    (r'^$', 'Papersreviews.search.views.search_page'),
)