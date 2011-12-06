from django.http import HttpResponse
from django.http import HttpResponseNotFound
from Papersreviews.papers.models import Papers
from Papersreviews.papers.models import Authors
from Papersreviews.papers.models import Files
from django.template import loader, Context, RequestContext
from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404
from django.db.models import Q
from django.core.paginator import Paginator
from Papersreviews.papers.forms import *
from django.core.context_processors import csrf
from filetransfers.api import serve_file

def index(request):
    PAPERS_PER_PAGE = 1
    page_tile = ''
    # get papers List
    pl = get_list_or_404(Papers)
    # get papers list per number
    paginator = Paginator(pl, PAPERS_PER_PAGE)
    # get authors List
    authors = get_list_or_404(Authors)
    # get files List
    files = get_list_or_404(Files)
    try:
        page_number = int(request.GET['page'])
    except (KeyError, ValueError):
            page_number = 1
    try:
        page = paginator.page(page_number)
    except InvalidPage:
        raise Http404
    papers = page.object_list
    authorsByPapers = getAuthorsByPapers(authors, papers)
    fileByPapers = getFileByPapers(files,papers)
    variables = RequestContext(request, {
    'papers': papers,
    'authors':authorsByPapers,
    'files':fileByPapers,
    'show_tags': True,
    'show_paginator': paginator.num_pages > 1,
    'has_prev': page.has_previous(),
    'has_next': page.has_next(),
    'page': page_number,
    'pages': paginator.num_pages,
    'next_page': page_number + 1,
    'prev_page': page_number - 1
    })
    form = SearchForm(request.GET)
    if form.is_valid():
        print form.cleaned_data['query']
    else:
        print 'not valid'
    return render_to_response('papers/body.html', variables)
    #return render_to_response('main/index.html', context_instance=RequestContext(request))
    
def getAuthorsByPapers(authors, papers):
    authorList = []
    for p in papers:
        for author in authors:
            if author.papers == p:
                authorList.append(author)
        return authorList
    return None
def getFileByPapers(files, papers):
    fileList = []
    for p in papers:
        for file in files:
            if file.papers == p:
                fileList.append(file)
        return fileList
    return None



