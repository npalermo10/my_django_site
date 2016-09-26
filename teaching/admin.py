from django.contrib import admin
from blog.models import Classroom, Announcements,Scheduled

class ClassroomAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}

class AnnouncementsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('date', 'classroom')}
    
# Register your models here.
admin.site.register(Classroom)
admin.site.register(Announcements)
admin.site.register(Scheduled)

