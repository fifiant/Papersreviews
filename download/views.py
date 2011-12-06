from django.http import HttpResponse
from django.http import HttpResponseNotFound
from Papersreviews.papers.models import Files
from django.template import loader, Context, RequestContext
from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404
from filetransfers.api import serve_file

def download(request, pid):
    # get the object by id or raise a 404 error
    object = get_object_or_404(Files, id=pid)

    return serve_file(request, object.file)