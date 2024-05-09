from django.contrib import admin

from .models import Publisher

class PublisherAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

admin.site.register(Publisher, PublisherAdmin)
