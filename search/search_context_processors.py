from shop.views import product_search
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank
from django.shortcuts import render
from .forms import SearchForm

def product_search(request):
    return {'form': form(request),
            'query': query(request),
            'results': results(request),
            'products':products(request),
            })


