from django.urls import path

from user.views import RegisterApiView, ActivationView, LoginApiView

urlpatterns = [
    path('register/', RegisterApiView.as_view()),
    path('login/', LoginApiView.as_view()),
    path('activate/<uuid:activation_code>/', ActivationView.as_view(), name='activate_account'),
]
# http://localhost.kg/sdas13213kllakdk21321lkaskdasdasd/