from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Post, Group


# Главная страница
def index(request):
    last_record = 10
    posts = Post.objects.order_by('-pub_date')[:last_record]
    context = {
        'posts': posts
    }
    return render(request, "posts/index.html", context)


def group_posts(request, slug):
    last_record = 10
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:last_record]
    context = {
        'group': group,
        'posts': posts
    }
    return render(request, "posts/group_list.html", context)
