from django.shortcuts import render_to_response
from photologue.models import Gallery
# Create your views here.
import pdb
def gallery_list(request):
    pdb.set_trace()
    return render_to_response("gallery_index.html",{'object_list':  Gallery.objects.all()})
