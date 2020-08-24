from django.contrib import admin
from .models import Category, Product, ProductImage, Contact, Subscription

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 0


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', ]
    prepopulated_fields = {'slug': ('name',)}
    list_filter = ['name', ]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'discounted_price', 'created', 'updated', 'discount','available',]
    search_fields = ('name', 'description')
    list_filter = ['available', 'created', 'updated','discount']
    list_editable = ['price', 'available', 'discount']
    inlines = [ProductImageInline]
    prepopulated_fields = {'slug': ('name',)}


@admin.register(ProductImage)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['product', 'image', 'available', 'created', 'updated',]


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'topic', 'message',]


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ['phone',]