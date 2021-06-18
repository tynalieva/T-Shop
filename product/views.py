from django.db.models import Q

from rest_framework import generics, permissions, viewsets, status
from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import action
from rest_framework.response import Response
from product.models import Product, Category, Like
from product.serializers import ProductSerializer, CategorySerializer
from django_filters.rest_framework import DjangoFilterBackend


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 1000


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    pagination_class = StandardResultsSetPagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category', ]

    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.query_params.get('search', '')
        if search:
            queryset = queryset.filter(
                Q(title__icontains=search) | Q(id__icontains=search) | Q(price__icontains=search))
        return queryset

    @action(detail=True, methods=['post'])
    def like(self, request, pk=None):
        product = self.get_object()
        obj, created = Like.objects.get_or_create(user=request.user.username, product=product)
        if not created:
            obj.like = not obj.like
            obj.save()
        liked_or_disliked = 'liked' if obj.like else 'disliked'
        return Response('Successfully {} product'.format(liked_or_disliked), status=status.HTTP_200_OK)


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
