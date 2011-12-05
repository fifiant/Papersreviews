from django.db import models
from ContentTypeRestrictedFileField import ContentTypeRestrictedFileField
class Papers(models.Model):
    """
    Papers to review
    """
    title = models.CharField(max_length=255, unique=True)
    abstract = models.TextField()
    def __unicode__(self):
        return self.title

class Authors(models.Model):
    """
    Papers Authors
    """
    name = models.CharField(max_length=255, unique=False)
    email = models.EmailField()
    papers = models.ForeignKey('Papers')
    def __unicode__(self):
        return self.name


class References(models.Model):
    """
    Papers References
    """
    description = models.TextField()
    papers = models.ForeignKey('Papers')
    def __unicode__(self):
        return self.description


class keywords(models.Model):
    """
    Papers keywords
    """
    title = models.CharField(max_length=300, unique=False)
    papers = models.ForeignKey('Papers')
    def __unicode__(self):
        return self.title

class Files(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    file = ContentTypeRestrictedFileField(
        upload_to='pdf',
        content_types=['application/pdf', 'application/zip', 'binary/octet-stream'],
        max_upload_size=5242880
    )
    created = models.DateTimeField('created', auto_now_add=True)
    modified = models.DateTimeField('modified', auto_now=True)
    papers = models.ForeignKey('Papers')
    def __unicode__(self):
        return self.name
