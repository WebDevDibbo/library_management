from django.urls import path
from .views import  CreateReviewView, DetailPost

urlpatterns = [
    path('add_review/<int:id>/', CreateReviewView.as_view(), name = 'submit_review'),
    path('details/<int:id>', DetailPost.as_view(), name = 'book_details'),
]
