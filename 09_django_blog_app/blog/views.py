from django.shortcuts import render

from rest_framework import viewsets

from .models import Category, Blog
from .serializers import CategorySerializer, BlogSerializer

class CategoryModelViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filterset_fields = ["name"]
    search_fields = ["name"]


class BlogModelViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    filterset_fields = ["cotegory__name", "cotegory"]
    search_fields = ["title", "content"]