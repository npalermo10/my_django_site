from .models import Post, Category
from django.shortcuts import render_to_response, get_object_or_404
from django.template import loader

def blog_index(request):
    recent_posts = Post.objects.all().order_by("posted")[:11]
    latest_post = recent_posts.reverse()[0]
    second_latest_post = recent_posts.reverse()[1]
    older_posts = recent_posts.reverse()[2:8]
    older_posts_grouped = zip(*[iter(older_posts)]*3)
    
    return render_to_response('blog_index.html', {
        'categories': Category.objects.all(),
        'latest_post': latest_post,
        'second_latest_post': second_latest_post,
        'older_posts_grouped': older_posts_grouped,
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
