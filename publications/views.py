from .models import Publication, Award
from django.shortcuts import render_to_response, get_object_or_404
from django.template import loader

# Create your views here.
def publication_index(request):
    return render_to_response("publication_index.html", {
        'publications':Publication.objects.all().order_by("-year"),
        'awards':Award.objects.all().order_by("-date")
         })
