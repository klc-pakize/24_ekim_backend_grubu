from django.shortcuts import render

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated

from .models import Departman, Personel
from .serializers import DepartmanSerializer, PersonelSerializer
from .permissions import IsStaffOrReadOnly, IsOwnerAndStaffOrReadOnly


class DepartmanListCreatAPIView(ListCreateAPIView):
    queryset = Departman.objects.all()
    serializer_class = DepartmanSerializer
    permission_classes = [IsAuthenticated, IsStaffOrReadOnly]

class DepartmanListAIPView(ListAPIView):
    # queryset = Departman.objects.all()
    serializer_class = DepartmanSerializer

    def get_queryset(self):
        name = self.kwargs["name"]
        return Departman.objects.filter(name__iexact=name)



class DepartmanDetail(RetrieveUpdateDestroyAPIView):
    queryset = Departman.objects.all()
    serializer_class = DepartmanSerializer
    permission_classes = [IsAuthenticated, IsStaffOrReadOnly]

class PersonelListCreateAPIView(ListCreateAPIView):
    queryset = Personel.objects.all().order_by('-salary')
    serializer_class = PersonelSerializer
    permission_classes = [IsAuthenticated, IsStaffOrReadOnly]


class PersonelDetail(RetrieveUpdateDestroyAPIView):
    queryset = Personel.objects.all()
    serializer_class = PersonelSerializer
    permission_classes = [IsAuthenticated, IsOwnerAndStaffOrReadOnly]