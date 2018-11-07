from django.contrib import admin
from movieapp.models import movie

class movieAdmin(admin.ModelAdmin):
    list_display = ['rdate','mname','hero','heroine','rating']
admin.site.register(movie,movieAdmin)

