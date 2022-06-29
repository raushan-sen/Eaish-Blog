from django.http.response import JsonResponse
from django.shortcuts import render
from .models import *
import datetime
import math

Seo=Seo_Setup.objects.all()[0]
ca=Seo.MainMenu.all()

def home(request):
    all_blogs=Blog.objects.all()
    all_blog_len=len(all_blogs)
    
    numberofposts=12

    p=request.GET.get('p')
    if p is None:
        page=1
    else:
        page=int(p)
    kamkablog=all_blogs[(page-1)*numberofposts:page*numberofposts]
    if page>1:
        prv=page-1
    else:
        prv=None

    if page<math.ceil(all_blog_len/numberofposts):
        nxt=page+1
    else:
        nxt=None
    context={
        'ca':ca,
        'numberofposts':numberofposts,
        'page':page,
        'nxt':nxt,
        'prev':prv,
        'seo':Seo,
        'pages':Page.objects.all()[:4],
        'all_blogs':kamkablog,
        'all_blog_len':all_blog_len,
    }
    return render(request,'index.html',context)



def blog(request,slug):
    try:
        if request.method=='POST':
            nm=request.POST['nm']
            comment=request.POST['comment']
            commenty=Comment(slug='blog/'+slug,name=nm,comment=comment,date=datetime.datetime.now())
            commenty.save()
            # return HttpResponse('suc')
        populars=Blog.objects.filter().order_by('-view')[:5]
        post=Blog.objects.filter(slug=str(slug))[0]
        commentsx=Comment.objects.filter(slug='blog/'+str(slug))
        singe=post.categery.all()
        latest=Blog.objects.all()[:5]
        pages=Page.objects.all()[:5]
        comments=Comment.objects.all()[:5]
        post.view=post.view+1
        post.save()
        context={
            'populars':populars,
            'commentsx':commentsx,
            'ca':ca,
            "singe":singe,
            'seo':Seo,
            'comments':comments,
            'pages':pages,
            'latests':latest,
            'blog':'blog/'+slug,
            'post':post,
        }
        return render(request,'article.html',context)
    except:
        context={
                'ca':ca,
                'seo':Seo,
                'pages':Page.objects.all()[:4],
            }
        return render(request,'404.html',context)

def search(request):
    query=request.GET['query']
    p=request.GET.get('p')
    posts=Blog.objects.filter(title__contains=str(query))
    numberofposts=12
    all_blog_len=len(posts)

    if len(posts)== 0:
        context={
            'ca':ca,
            'seo':Seo,
            'pages':Page.objects.all()[:4],
            
        }
        
        return render(request,'404.html',context)
    else:
        if p is None:
            page=1
        else:
            page=int(p)

        kamkablog=posts[(page-1)*numberofposts:page*numberofposts]
        
        if page>1:
            prv=page-1
        else:
            prv=None

        if page<math.ceil(all_blog_len/numberofposts):
            nxt=page+1
        else:
            nxt=None

        context={
            'ca':ca,
            "text":"You Have Searched",
            'numberofposts':numberofposts,
            'pages':Page.objects.all()[:4],
            'page':page,
            'nxt':nxt,
            'prev':prv,
            'seo':Seo,
            'all_blog_len':all_blog_len,
            'query':query,
            'all_posts':kamkablog,
            }
        return render(request,'search.html',context)


def page(request,slug):
    try:
        if request.method=='POST':
            nm=request.POST['nm']
            comment=request.POST['comment']
            comment=Comment(slug='page/'+slug,name=nm,comment=comment,date=datetime.datetime.now())
            comment.save()
        
        post=Page.objects.filter(slug=str(slug))[0]
        commentsx=Comment.objects.filter(slug='page/'+str(slug))
        
        post.view=post.view+1
        post.save()
        latest=Blog.objects.all()[:5]
        populars=Blog.objects.filter().order_by('-view')[:5]
        pages=Page.objects.all()[:5]
        comments=Comment.objects.all()[:5]
        context={
            'populars':populars,
            'commentsx':commentsx,
            'ca':ca,
            'seo':Seo,
            'comments':comments,
            'pages':pages,
            'latests':latest,
            'blog':'page/'+slug,
            'post':post,
        }
        return render(request,'article.html',context)
    except:
        context={
                'ca':ca,
                'seo':Seo,
                'pages':Page.objects.all()[:4],
            }
        return render(request,'404.html',context)


def category(request,category):

    try:
        categor=Categery.objects.filter(slug=category)[0]
        blogs=Categery.objects.distinct()
        numberofposts=12
        for sin in blogs:
            if sin.slug==category:
                ff=Blog.objects.filter(categery__id=sin.pk)
        
        if len(ff)== 0:
            context={
                'ca':ca,
                'seo':Seo,
                'pages':Page.objects.all()[:4],
            }
        
            return render(request,'404.html',context)
        else:
            context={
                'ca':ca,
                'seo':Seo,
                "text":"Category Name ",
                "numberofposts":numberofposts,
                'pages':Page.objects.all()[:4],
                "all_blog_len":len(ff),
                "query":categor.name,
                "all_posts":ff,
            }

            return render(request,'search.html',context)
    except:
        context={
                'ca':ca,
                'seo':Seo,
                'pages':Page.objects.all()[:4],
            }
        return render(request,'404.html',context)

