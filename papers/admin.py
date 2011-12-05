from django.contrib import admin
from Papersreviews.papers.models import Papers
from Papersreviews.papers.models import Authors
from Papersreviews.papers.models import References
from Papersreviews.papers.models import keywords
from Papersreviews.papers.models import Files

admin.site.register(Papers)
admin.site.register(Authors)
admin.site.register(References)
admin.site.register(keywords)
admin.site.register(Files)