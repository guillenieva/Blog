from django.contrib import admin
from .models import *

# Register your models here.

class PublicacionAdmin(admin.ModelAdmin):
    readonly_fields = ["id"]
    list_display = ["id", "titulo","cuerpo"]
    list_display_links = ["id", "titulo","cuerpo"]
    search_fields = ["titulo"]

admin.site.register(Publicacion, PublicacionAdmin)
