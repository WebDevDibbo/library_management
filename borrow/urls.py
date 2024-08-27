from django.urls import path
from .views import borrow

urlpatterns = [
    path('borrow_book/<int:id>', borrow, name = 'borrow_book'),
]
