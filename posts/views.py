import time

from django.shortcuts import render
from django.http import request, HttpResponseRedirect
# Create your views here.
from posts.models import Posts
from datetime import  datetime


def redirect_home(request):
    return HttpResponseRedirect('/home/')


def home(request):
    return render(request, "index.html")


def lista_posts(request):
    lista_posts = Posts.objects.all().order_by('data')
    return render(request, "posts.html", {'lista_posts': lista_posts})


def postar(request):
    if request.method == "POST":
        posts = Posts()
        posts.nome = request.POST.get('nome', None)
        posts.descricao = request.POST.get('descricao', None)
        posts.data = datetime.utcnow()
        posts.save()
        return HttpResponseRedirect('/home/')

