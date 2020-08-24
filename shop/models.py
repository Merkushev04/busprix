from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse ('shop:product_list_by_category', args=[self.slug])

class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=0)
    discounted_price = models.DecimalField(default=1, max_digits=10, decimal_places=0, blank=True)
    discount = models.BooleanField(default=False, blank=True)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)

    index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.id, self.slug])


class ProductImage(models.Model):
    product = models.ForeignKey(Product, blank=True, default=None, on_delete=models.CASCADE)
    image_name = str(product)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.image_name

    class Meta:
        ordering = ('product',)


class Contact(models.Model):
    name = models.CharField(max_length=200, db_index=True, verbose_name='Ваше имя')
    email = models.CharField(max_length=200, db_index=True, verbose_name='Ваш email')
    topic = models.CharField(max_length=200, db_index=True, verbose_name='Тема сообщения')
    message = models.TextField(blank=True, verbose_name='Ваше сообщение')
    # message = models.CharField(max_length=800, db_index=True, verbose_name='Ваше сообщене')

    def __str__(self):
        return self.name

