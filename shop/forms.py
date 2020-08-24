from django import forms
from .models import Product, Contact


class CommentForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'description', )


class SearchForm(forms.Form):
    query = forms.CharField()


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'topic', 'message',]

