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

def search_page(request):
    form = SearchForm()
    papers = []
    authorsByPapers = []
    fileByPapers = []
    show_results = False
    if 'query' in request.GET:
        #show_results = True
        query = request.GET['query'].strip()
        if query:
            keywords = query.split()
            q = Q()
            q1 = Q()
            # Set Query research here
            for keyword in keywords:
                q = q & Q(title__icontains=keyword)
                q1 = q1 & Q(abstract__icontains=keyword)
                print q, q1
            form = SearchForm({'query' : query})
            #papers = Papers.objects.filter(q)[:10]
            for p in Papers.objects.filter(q)[:10]:
                papers.append(p)
            for p1 in Papers.objects.filter(q1)[:10]:
                papers.append(p1)
            # Eliminate duplicated object in the List
            papers = set(papers)    
            if papers:
                show_results = True
            # get authors List
            authors = get_list_or_404(Authors)
            # get files List
            files = get_list_or_404(Files)
            authorsByPapers = getAuthorsByPapers(authors, papers)
            fileByPapers = getFileByPapers(files,papers)
            for p in papers:
                print p
    variables = RequestContext(request, {
    'form': form,
    'papers': papers,
    'authors':authorsByPapers,
    'files':fileByPapers,
    'show_results': show_results,
    })
    return render_to_response('search/body.html', variables)


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
            