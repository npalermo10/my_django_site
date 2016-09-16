from django.contrib import admin
from current_research.models import Curr_research, Category

# Register your models here.

class Curr_researchAdmin(admin.ModelAdmin):
    # exclude = ['posted']
    prepopulated_fields = {'slug': ('title',)}

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    
admin.site.register(Curr_research)
admin.site.register(Category)
