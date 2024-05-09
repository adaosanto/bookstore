from django.contrib import admin

from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'language', 'genre', 'publisher', 'publication_year', 'pages')

admin.site.register(Book, BookAdmin)
