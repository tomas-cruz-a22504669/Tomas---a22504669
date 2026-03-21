from django.contrib import admin

# Register your models here.
from .models import Festival, Banda

class FestivalAdmin(admin.ModelAdmin):
    list_display = ("nome", "local")
    search_fields = ("nome",)

class BandaAdmin(admin.ModelAdmin):
    list_display = ("nome", "estilo")
    search_fields = ("nome",)

admin.site.register(Festival, FestivalAdmin)
admin.site.register(Banda, BandaAdmin)