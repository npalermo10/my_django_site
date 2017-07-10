from django.shortcuts import render_to_response
from photologue.models import Gallery
# Create your views here.

def gallery_list(request):
    return render_to_response("gallery_index.html",{'object_list':  Gallery.objects.all()})
