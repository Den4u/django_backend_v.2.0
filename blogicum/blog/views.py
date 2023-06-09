from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.db.models import Q
from django.core.paginator import Paginator

from .models import Category, Post


def index(request):
    posts = Post.objects.all().filter(
        is_published=True,
        category__is_published=True,
        pub_date__lte=timezone.now())
    paginator = Paginator(posts, 5)
    posts = paginator.page(1)
    template = 'blog/index.html'
    context = {'post_list': posts}
    return render(request, template, context)


def post_detail(request, post_id):
    post = get_object_or_404(
        Post.objects.select_related(
            'author', 'location').filter(
            pub_date__lte=timezone.now(),
            is_published=True,
            category__is_published=True),
        pk=post_id
    )
    template = 'blog/detail.html'
    context = {'post': post}
    return render(request, template, context)


def category_posts(request, category_slug):
    category = get_object_or_404(
        Category,
        slug=category_slug,
        is_published=True
    )
    post_list = Post.objects.filter(
        Q(category=category)
        & Q(is_published=True)
        & Q(pub_date__lte=timezone.now())
    )
    template = 'blog/category.html'
    context = {
        'category': category,
        'post_list': post_list
    }
    return render(request, template, context)
