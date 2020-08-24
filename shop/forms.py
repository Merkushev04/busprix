from django import forms
from .models import Product, Contact, Subscription


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


class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = Subscription
        fields = ('phone',)
