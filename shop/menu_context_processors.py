from .models import Category, Product


def category(request):
    return {"categories": Category.objects.all()}

def products(request):
    return {"products": Product.objects.all(),}

