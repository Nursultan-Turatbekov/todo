from django.contrib import admin
from .models import ToDo
from .models import Book

admin.site.register(ToDo)
admin.site.register(Book)

# Register your models here.
