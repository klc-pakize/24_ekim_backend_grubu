from django.urls import path, include

from .views import DepartmanListCreatAPIView, PersonelListCreateAPIView, DepartmanDetail, PersonelDetail,DepartmanListAIPView

urlpatterns = [
    path('departman/', DepartmanListCreatAPIView.as_view()),
    path('departman/<int:pk>/', DepartmanDetail.as_view()),
    path('departman/<str:name>/', DepartmanListAIPView.as_view()),
    path('', PersonelListCreateAPIView.as_view()),
    path('<int:pk>/', PersonelDetail.as_view()),
]
