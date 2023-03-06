from django.contrib import admin

from .models import *
from .project_models import *
# Register your models here.

admin.site.register(Hobby)
admin.site.register(Team)
admin.site.register(Project)
admin.site.register(Description)

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):    
    list_display = ['name']

@admin.register(Candidate)
class CandidateAdmin(admin.ModelAdmin):
    list_display = ['full_name']


admin.site.register(SkillTitle)
admin.site.register(SkillDescription)
admin.site.register(Content)

