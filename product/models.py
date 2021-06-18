from django.db import models
from user.models import CustomUser


class DataABC(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Category(models.Model):
    name = models.CharField(max_length=150)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True,blank=True, related_name='children')

    def __str__(self):
        if not self.parent:
            return f"{self.name}"
        else:
            return f"{self.parent} -->{self.name}"

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'


class Product(DataABC):
    # id = models.BigIntegerField(primary_key=True, )
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    user = models.ForeignKey(CustomUser, related_name='products', on_delete=models.CASCADE, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', null=True)


class ProductImage(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    image = models.ImageField(upload_to='images/')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')

    class Meta:
        verbose_name = 'image'
        verbose_name_plural = 'images'

    @staticmethod
    def generate_name():
        import random
        return "image" + str(random.randint(111111, 999999))

    def save(self, *args, **kwargs):
        self.title = self.generate_name()
        return super(ProductImage, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.title} --> {self.product.id}'


class Like(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='likes')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='likes')
    likes = models.BooleanField(default=False)

    def str(self):
        return f'{self.user} liked this movie--> {self.product}'


class Feedback(models.Model):
    user = models.ForeignKey(CustomUser, related_name='feedbacks', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='feedbacks', on_delete=models.CASCADE)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user}-->{self.product}-->{self.created_at}"