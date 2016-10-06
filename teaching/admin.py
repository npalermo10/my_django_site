from django.contrib import admin
from teaching.models import Classroom, Announcement,Scheduled

class ClassroomAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}

class AnnouncementAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('date', 'classroom')}
    
# Register your models here.
admin.site.register(Classroom)
admin.site.register(Announcement)
admin.site.register(Scheduled)
