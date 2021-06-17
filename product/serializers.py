from rest_framework import serializers
from product.models import Product, ProductImage, Category
from user.models import CustomUser


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'parent')

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if instance.children.exists():
            representation['children'] = CategorySerializer(instance=instance.children.all(), many=True).data

        return representation


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage


class ProductSerializer(serializers.ModelSerializer):
    # user = serializers.ReadOnlyField(source=CustomUser.username)
    category = CategorySerializer(many=False, read_only=True)
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
