from .models import Classroom, Announcement, Scheduled
from django.shortcuts import render_to_response, get_object_or_404
from django.template import loader
import pdb

# Create your views here.
def teaching_index(request):
    return render_to_response("teaching_index.html", {
        'classrooms':Classroom.objects.all().order_by("-year"),
         })

def view_classroom(request, slug):
    return render_to_response("classroom_index.html", {
        'classroom':get_object_or_404(Classroom, slug=slug),
        'announcement': Announcement.objects.filter(slug__slug=slug),
        'scheduled':Scheduled.objects.all().filter(slug__slug=slug).order_by("-date"),
            }
    )
    pdb.set_trace()
