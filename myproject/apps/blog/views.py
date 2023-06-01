from django.shortcuts import render, get_object_or_404
from .models import Post, Category

def list(request):
    facets = {
        "categories": {
            "keterangan": Category.objects.values_list('id','title').distinct()
        },
    }

    if request.GET.get('keterangan'):
        if request.GET.get('keterangan') == 'semua':
            posts = Post.objects.filter(status=Post.ACTIVE)
        else:
            posts = Post.objects.filter(category=request.GET.get('keterangan'), status=Post.ACTIVE)
    else:
        posts = Post.objects.filter(status=Post.ACTIVE)

    context = {
        'posts': posts,
        'facets': facets
    }

    return render(request, 'blog/blog_list.html', context)

def detail(request, category_slug, slug):
    post = get_object_or_404(Post, slug=slug, status=Post.ACTIVE)

    context = {
        'post': post,
        'slug': slug,
        'category_slug': category_slug,
    }

    return render(request, 'blog/blog_detail.html', context)