from django.conf.urls.defaults import *
from Papersreviews.papers.models import Papers

urlpatterns = patterns('',
    (r'^(?P<pid>\d+)/$', 'Papersreviews.download.views.download'),
)