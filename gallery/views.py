from .models import Album, Photo
from django.shortcuts import render_to_response, get_object_or_404
from django.template import loader

def gallery_index(request):
    return render_to_response("gallery_index.html", {
        "albums":Album.objects.all().order_by("-year"),
        })

def view_album(request,slug):
    return render_to_response("album_index.html", {
        "album": Album.objects.filter(slug__slug=slug),
        "photos":Photo.objects.filter(slug__slug=slug),
        })
