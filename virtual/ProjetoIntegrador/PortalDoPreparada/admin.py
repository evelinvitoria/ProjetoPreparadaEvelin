from django.contrib import admin
from .models import profissionais


class profissionalAdmin(admin.ModelAdmin):
    list_display = ('nome', 'competencia')
    search_fields = ('nome',)
    list_per_page = int = 3
    model = profissionais

admin.site.register(profissionais, profissionalAdmin)

# Register your models here.