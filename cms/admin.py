from django.contrib import admin
from cms.models import *

@admin.register(Slider)
class Slider(admin.ModelAdmin):
    list_display = [field.name for field in Slider._meta.fields]

@admin.register(Project)
class Project(admin.ModelAdmin):
    list_display = [field.name for field in Project._meta.fields]

@admin.register(AboutUs)
class AboutUs(admin.ModelAdmin):
    list_display = [field.name for field in AboutUs._meta.fields]
    
@admin.register(SisterConcern)
class SisterConcern(admin.ModelAdmin):
    list_display = [field.name for field in SisterConcern._meta.fields]
    
@admin.register(Team)
class Team(admin.ModelAdmin):
    list_display = [field.name for field in Team._meta.fields]
    
@admin.register(Counter)
class Counter(admin.ModelAdmin):
    list_display = [field.name for field in Counter._meta.fields]
    
@admin.register(Blog)
class Blog(admin.ModelAdmin):
    list_display = [field.name for field in Blog._meta.fields]
    
@admin.register(CompanyInfo)
class CompanyInfo(admin.ModelAdmin):
    list_display = [field.name for field in CompanyInfo._meta.fields]

@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')  # Customize the columns displayed
    search_fields = ('name', 'email')  # Enable search functionality
    list_filter = ('created_at',)  # Enable filtering