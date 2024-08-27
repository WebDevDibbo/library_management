from django.contrib import admin
from .models import Categories, BookModel, Review

# Register your models here.
admin.site.register((Categories,BookModel,Review))