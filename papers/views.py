from django.http import HttpResponse
from django.http import HttpResponseNotFound
from Papersreviews.papers.models import Papers
from Papersreviews.papers.models import Authors
from django.template import loader, Context, RequestContext
from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404
from django.db.models import Q
from django.core.paginator import Paginator
from Papersreviews.papers.forms import *
from django.core.context_processors import csrf

def index(request):
    PAPERS_PER_PAGE = 1
    page_tile = ''
    pl = get_list_or_404(Papers)
    paginator = Paginator(pl, PAPERS_PER_PAGE)
    try:
        page_number = int(request.GET['page'])
    except (KeyError, ValueError):
            page_number = 1
    try:
        page = paginator.page(page_number)
    except InvalidPage:
        raise Http404
    papers = page.object_list
    authors = get_list_or_404(Authors)
    authorsByPapers = getAuthorsByPapers(authors, pl)
    for a in getAuthorsByPapers(authors, pl):
        print a.name
    variables = RequestContext(request, {
    'papers': papers,
    'authors':authorsByPapers,
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
        print form.cleaned_data['key']
    else:
        print 'not valid'
    #t = loader.get_template('body.html')
    c = Context({'papers': pl, 'authors':authorsByPapers})
    #return HttpResponse(t.render(c))
    return render_to_response('body.html', variables)
    #return render_to_response('main/index.html', context_instance=RequestContext(request))
    
def getAuthorsByPapers(authors, papers):
    authorList = []
    for p in papers:
        for author in authors:
            if author.papers == p:
                authorList.append(author)
        return authorList
    return None

def search_page(request):
    form = SearchForm()
    papers = []
    show_results = False
    if 'query' in request.GET:
        show_results = True
        query = request.GET['query'].strip()
        if query:
            keywords = query.split()
            q = Q()
            for keyword in keywords:
                q = q & Q(title__icontains=keyword)
            form = SearchForm({'query' : query})
            bookmarks = Bookmark.objects.filter(q)[:10]
    variables = RequestContext(request, {
    'form': form,
    'papers': papers,
    'show_results': show_results,
    'show_tags': True,
    'show_user': True
    })
    return render_to_response('body.html', variables)



