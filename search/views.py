from django.shortcuts import render, get_object_or_404
from shop.models import Category, Product, ProductImage
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank
from shop.forms import SearchForm, CommentForm

def product_search(request):
    form = SearchForm()
    query = None
    results = []
    products = Product.objects.all()
    if 'query' in request.GET:
        form = SearchForm(request.GET)
    if form.is_valid():
        query = form.cleaned_data['query']
        search_vector = SearchVector('name', weight='A') + SearchVector('description', weight='B')
        search_query = SearchQuery(query)
        results = Product.objects.annotate(
            search=search_vector,
            rank=SearchRank (search_vector, search_query)
        ).filter(rank__gte=0.3).order_by('-rank')
        # results = Product.objects.annotate(similarity=TrigramSimilarity('name', query),).filter(similarity__gt=0.3).order_by('-similarity')
    return render(request, 'shop/product/search.html', {'form': form,
                                                     'query': query,
                                                     'results': results,
                                                     'products':products,
                                                        })
