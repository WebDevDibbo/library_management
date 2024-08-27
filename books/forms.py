from django import forms
from .models import Categories, BookModel, Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['body']