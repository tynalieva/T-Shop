from django.urls import path, include
from product import views


urlpatterns = [
    path('products/', views.PostList.as_view()),
    path('products/<int:pk>/', views.PostDetail.as_view()),
    path('categories/', views.CategoryView.as_view()),
]