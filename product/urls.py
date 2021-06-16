from django.urls import path, include
from rest_framework.routers import DefaultRouter
from product import views


urlpatterns = [
    path('', views.PostList.as_view()),
    path('<int:pk>/', views.PostDetail.as_view()),
]