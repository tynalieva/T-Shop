from django.contrib import admin
from product.models import Product, Category, ProductImage, Like, Feedback

admin.site.register(Product)
admin.site.register(ProductImage)
admin.site.register(Category)
admin.site.register(Like)
admin.site.register(Feedback)

