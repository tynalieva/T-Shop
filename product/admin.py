from django.contrib import admin
from product.models import Product, Category, ProductImage

admin.site.register(Product)
admin.site.register(ProductImage)
admin.site.register(Category)
