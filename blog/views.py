from .models import Post, Category
from django.shortcuts import render_to_response, get_object_or_404
from django.template import loader

def blog_index(request):
    latest_post = Post.objects.latest("posted")
    return render_to_response('blog_index.html', {
        'categories': Category.objects.all(),
        'posts': Post.objects.all()[:5],
        'latest_post': latest_post
        })

def view_post(request, slug):
    return render_to_response('view_post.html', {
        'post': get_object_or_404(Post, slug=slug)
        })

def view_category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    return render_to_response('view_category.html', {
        'category': category,
        'posts': Post.objects.filter(category=category)[:5]
        })
