from django.contrib import admin
from publications.models import Publication, Award

# Register your models here.

class Publications_Admin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

class Awards_Admin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    
admin.site.register(Publication)
admin.site.register(Award)
