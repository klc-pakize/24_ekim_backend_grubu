from django.urls import path, include

from rest_framework.authtoken import views

from .views import RegisterCreateAPIView, logout

urlpatterns = [
    path("register/", RegisterCreateAPIView.as_view()),
    path('login/', views.obtain_auth_token),
    path('logout/', logout),
]