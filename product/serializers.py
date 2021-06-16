from rest_framework import serializers
from product.models import Product, ProductImage


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage


class ProductSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = '__all__'

    def create(self, validated_data):
        print(validated_data)
        request = self.context.get('request')
        images_data = request.FILES
        created_post = Product.objects.create(**validated_data)
        print(created_post)
        images_obj = [ProductImage(post=created_post, image=image)
                      for image in images_data.getlist('images')]
        ProductImage.objects.bulk_create(images_obj)
        return created_post
