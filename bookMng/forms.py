from django import forms
from django.forms import ModelForm, CharField, URLField, DecimalField, FileField
from .models import Book, Search

class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = [
            'name',
            'web',
            'price',
            'picture',
        ]

class SearchForm(ModelForm):
    class Meta:
        model = Search
        fields = [
            'name'
        ]
