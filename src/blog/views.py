from django.shortcuts import render,redirect,reverse,get_object_or_404
import os
from src.settings import ARTICLE_ROOT
# Create your views here.
import markdown
from django.db.models import Q
from .models import Article
def index(request):
    return render(request, 'blog/index.html')
def detail(request):
    CSDNurl='https://me.csdn.net/qq_44720314'
    article = Article.objects.order_by('-id').first()
    e_time = article.modified_time
    column = article.column
    columns = Article.objects.all().values('column').distinct()
    article.body = markdown.markdown(article.body,
                                     extensions=['markdown.extensions.extra',
                                                 'markdown.extensions.codehilite',
                                         'markdown.extensions.toc', ],
                                        safe_mode=True, enable_attributes=False)

    return render(request, 'blog/blog.html', context={
        'article':article,
        'e_time':e_time,
        'column':column,
        'columns':columns,
        'CSDNurl':CSDNurl
    })

def list(request,column):
    articles = Article.objects.filter(column=column)
    return render(request,'blog/list.html',context={
        'articles':articles,
        'column':column,
    })
def detail2(request,pk):
    CSDNurl='https://me.csdn.net/qq_44720314'
    article = Article.objects.get(pk=pk)
    e_time = article.modified_time
    column = article.column
    columns = Article.objects.all().values('column').distinct()
    article.body = markdown.markdown(article.body,
                                     extensions=['markdown.extensions.extra',
                                                 'markdown.extensions.codehilite',
                                         'markdown.extensions.toc', ],
                                        safe_mode=True, enable_attributes=False)

    return render(request, 'blog/blog.html', context={
        'article':article,
        'e_time':e_time,
        'column':column,
        'columns':columns,
        'CSDNurl':CSDNurl
    })