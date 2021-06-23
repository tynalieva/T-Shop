from django.urls import path
from product import views


urlpatterns = [
    path('categories/', views.CategoryView.as_view()),
    path('products/', views.ProductListCreateView.as_view()),
    path('products/<int:pk>/', views.ProductRetrieveUpdateDestroyView.as_view()),
    path('feedbacks/', views.FeedbackListCreateView.as_view()),
    path('feedbacks/<int:pk>/', views.FeedbackDetailView.as_view()),
    path('likes/', views.LikeListCreateView.as_view()),
    path('likes/<int:pk>/', views.LikeDetailView.as_view()),
]