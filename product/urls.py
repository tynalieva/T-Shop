from django.urls import path, include
from rest_framework.routers import DefaultRouter
from product import views


router = DefaultRouter()
router.register('products', views.ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('categories/', views.CategoryView.as_view()),
    path('feedbacks/', views.FeedbackListCreateView.as_view()),
    path('feedbacks/<int:pk>/', views.FeedbackDetailView.as_view()),
    path('likes/', views.LikeListCreateView.as_view()),
    path('likes/<int:pk>/', views.LikeDetailView.as_view()),
]