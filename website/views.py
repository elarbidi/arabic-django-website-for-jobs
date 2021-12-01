from django.shortcuts import render
from .models import les_post
from django.core.paginator import Paginator


# Create your views here.
def index(request):
    one = les_post.objects.filter()[:1]
    main_Post = les_post.objects.all()[1:50]
    paginator = Paginator(main_Post, 6) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'Post' : page_obj ,
        'one' : one
    }
    return render(request,'index.html', context)

def tawjih(request):
    one = les_post.objects.filter(categorie__le_nom='Tawjih')[:1]
    main_Post = les_post.objects.filter(categorie__le_nom='Tawjih')[1:50]
    paginator = Paginator(main_Post, 6) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'Post' : page_obj ,
        'one' : one
    }
    return render(request,'tawjih.html', context)

def anapec(request):
    one = les_post.objects.filter(categorie__le_nom='anapec')[:1]
    main_Post = les_post.objects.filter(categorie__le_nom='anapec')[1:50]
    paginator = Paginator(main_Post, 6) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'Post' : page_obj ,
        'one' : one
    }
    return render(request,'anapec.html', context)

def stage(request):
    one = les_post.objects.filter(categorie__le_nom='stage')[:1]
    main_Post = les_post.objects.filter(categorie__le_nom='stage')[1:50]
    paginator = Paginator(main_Post, 6) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'Post' : page_obj ,
        'one' : one
    }
    return render(request,'stage.html', context)

def jobs(request):
    one = les_post.objects.filter(categorie__le_nom='jobs')[:1]
    main_Post = les_post.objects.filter(categorie__le_nom='jobs')[1:50]
    paginator = Paginator(main_Post, 6) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'Post' : page_obj ,
        'one' : one
    }
    return render(request,'jobs.html', context)
def talaba(request):
    one = les_post.objects.filter(categorie__le_nom='anapec')[:1]
    main_Post = les_post.objects.filter(categorie__le_nom='anapec')[1:50]
    paginator = Paginator(main_Post, 6) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'Post' : page_obj ,
        'one' : one
    }
    return render(request,'talaba.html', context)

def city(request , city):
    one = les_post.objects.filter(villes__le_nom=city)[:1]
    main_Post = les_post.objects.filter(villes__le_nom=city)[1:50]
    paginator = Paginator(main_Post, 6) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'Post' : page_obj ,
        'one' : one,
        'city' : city
    }
    return render(request,'city.html', context)

def article(request , slug):
    Post = les_post.objects.filter(slug=slug)
    context = {
        'Post' : Post
    }
    return render(request,'article.html', context)

def handler404(request, exception):
    return render(request,'404.html')

def teq(request):
    one = les_post.objects.filter(categorie__le_nom='teq')[:1]
    main_Post = les_post.objects.filter(categorie__le_nom='teq')[1:50]
    paginator = Paginator(main_Post, 6) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'Post' : page_obj ,
        'one' : one
    }
    return render(request,'teq.html', context)