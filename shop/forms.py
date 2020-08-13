from django import forms
from .models import Product


class CommentForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'description', )


class SearchForm(forms.Form):
    query = forms.CharField()

