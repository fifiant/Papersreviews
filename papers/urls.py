from django.conf.urls.defaults import *
from Papersreviews.papers.models import Papers

urlpatterns = patterns('',
    #(r'^(?P<pid>\d+)/$', 'fifiant.main.views.index'),
    (r'^$', 'Papersreviews.papers.views.index'),
    (r'^search/$', 'Papersreviews.papers.views.search_page'),
)