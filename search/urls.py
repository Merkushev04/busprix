from django.urls import path
from . import views


app_name = 'cart'

urlpatterns = [
    path('', views.search, name='search'),
    path('products/search/', views.product_search, name='product_search'),
]