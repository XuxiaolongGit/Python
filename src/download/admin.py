from django.contrib import admin

# Register your models here.
from .models import Book
admin.site.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['id','name','size','uploader']

    list_per_page = 10