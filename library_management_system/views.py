from django.shortcuts import render
from django.views.generic import TemplateView
from books.models import BookModel, Categories




def home(request, category_slug = None):
    data = BookModel.objects.all()
    print(BookModel.objects.get(pk=1))
    if category_slug is not None:
        category = Categories.objects.get(slug = category_slug)
        data = BookModel.objects.filter(category = category)
    categories = Categories.objects.all()
    return render(request, 'home.html', {'data':data, 'category' : categories})