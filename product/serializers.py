from rest_framework import serializers
from product.models import Product, ProductImage, Category, Like, Feedback
from user.models import CustomUser


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name',)


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        exclude = ('id', )


class ProductSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.email')
    category = CategorySerializer(many=False, read_only=True)
    images = ProductImageSerializer(many=True, read_only=True)
    feedbacks = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    likes = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ('id', 'user', 'category', 'title', 'description', 'price', 'images', 'likes', 'feedbacks', 'created_at', 'updated_at')

    def create(self, validated_data):
        request = self.context.get('request')
        images_data = request.FILES
        product = Product.objects.create(**validated_data)
        print(images_data.getlist('images'))
        for image in images_data.getlist('images'):
            ProductImage.objects.create(product=product, image=image)
        return product


class FeedbackSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.email')

    class Meta:
        model = Feedback
        fields = ('id', 'user', 'product', 'body')


class LikeSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.email')

    class Meta:
        model = Like
        fields = '__all__'
