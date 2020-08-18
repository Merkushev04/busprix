from django.urls import path, include
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('products/', views.product_list, name='product_list'),
    path('contact/', views.contact, name='contact'),
    path('product_search/', views.product_search, name='product_search'),
    path('<slug:category_slug>/', views.product_list,name='product_list_by_category'),
    path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),
    # path('products/search/', views.product_search, name='product_search'),
]