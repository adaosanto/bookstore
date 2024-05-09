from django.contrib import admin

from .models import Language

class LanguageAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

admin.site.register(Language, LanguageAdmin)
