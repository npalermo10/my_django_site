from .models import Publication, Award
from django.shortcuts import render_to_response, get_object_or_404
from django.template import loader

# Create your views here.
def teaching_index(request):
    return render_to_response("teaching_index.html", {
        'classrooms':Classroom.objects.all().order_by("-year"),
         })
