from django import forms
from download.models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        exclude = ['uploader']