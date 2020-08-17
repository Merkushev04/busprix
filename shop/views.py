from django.shortcuts import render, get_object_or_404
from .models import Category, Product, ProductImage
from cart.forms import CartAddProductForm
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank
from shop.forms import SearchForm, CommentForm

def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True, )
    if category_slug:
        category = get_object_or_404 (Category, slug=category_slug)
        products = products.filter (category=category)
    return render (request, 'shop/product/list.html',
                   {'category': category,
                    'categories': categories,
                    'products': products,
                    })


def product_detail(request, id, slug,):
    product = get_object_or_404 (Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    additional_images = ProductImage.objects.all()
    return render(request, 'shop/product/detail.html', {'product': product,
                                                        'cart_product_form': cart_product_form,
                                                        'additional_images': additional_images,
                                                        })

def home_page(request):
    products = Product.objects.all()
    return render(request, 'shop/base.html', {'products': products,})


def product_search(request):
    form = SearchForm()
    query = None
    results = []
    search_products = Product.objects.all()
    if 'query' in request.GET:
        form = SearchForm(request.GET)
    if form.is_valid():
        query = form.cleaned_data['query']
        search_vector = SearchVector('name', weight='A') + SearchVector('description', weight='B')
        search_query = SearchQuery(query)
        results = Product.objects.annotate(
            search=search_vector,
            rank=SearchRank(search_vector, search_query)
        ).filter(rank__gte=0.3).order_by('-rank')
        # results = Product.objects.annotate(similarity=TrigramSimilarity('name', query),).filter(similarity__gt=0.3).order_by('-similarity')
    return render(request, 'shop/product/search.html', {'form': form,
                                                        'query': query,
                                                        'results': results,
                                                        'search_products': search_products,
                                                        })

