from .models import Curr_research
from django.shortcuts import render_to_response, get_object_or_404
from django.template import loader

# Create your views here.
def current_research(request):
    return render_to_response("curr_research.html", {
        'research_description':Curr_research.objects.all(),
        'research_category':Category.objects.all()
        })

