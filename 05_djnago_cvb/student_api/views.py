from django.shortcuts import render, HttpResponse, get_object_or_404

from .models import Student, Path

from .serializers import StudentSerializer, PathSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


from rest_framework.views import APIView

from rest_framework.generics import GenericAPIView, mixins

from rest_framework.generics import ListCreateAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView

from rest_framework.viewsets import ModelViewSet


@api_view(['GET'])
def home(request):
    return Response({"home": "This is home page..."})


# http methods ----------->
# - GET (DB den veri çağırma, public)
# - POST(DB de değişklik, create, private)
# - PUT (DB DE KAYIT DEĞİŞKLİĞİ, private)
# - delete (dB de kayıt silme)
# - patch (kısmi update)


#!#################### FUNCTION BASED VIEWS ########################################

@api_view(['GET'])
def butun_ogrencileri_getir(request):
    ogrenciler_queryset_tipinde_data = Student.objects.all()
    # print(ogrenciler_queryset_tipinde_data)
    tip_donusumu = StudentSerializer(ogrenciler_queryset_tipinde_data, many=True)
    return Response(tip_donusumu.data)


@api_view(['POST'])
def yeni_ogreci_create_et(request):
    print(request.data)
    json_formatın_queyset_donum = StudentSerializer(data=request.data)
    if json_formatın_queyset_donum.is_valid():
        json_formatın_queyset_donum.save()
        return Response(json_formatın_queyset_donum.data, status=status.HTTP_201_CREATED)
    return Response(json_formatın_queyset_donum.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view()
def tek_ogrenciyi_goruntuleme_islemi(request, pk):
    # try:
    #     tek_ogrenci = Student.objects.get(id=pk)
    #     serializer = StudentSerializer(tek_ogrenci)
    #     return Response(serializer.data)
    # except:
    #     return Response({"message": "olmayan id numarası girildi. id numranı kontrold et!!!!"})

    tek_ogrenci = get_object_or_404(Student, id=pk)
    serializer = StudentSerializer(tek_ogrenci)
    return Response(serializer.data)


        
    
@api_view(['PUT'])
def qorenciyi_guncelle(request, pk):
    tek_ogenci = get_object_or_404(Student, id=pk)
    serilaizer = StudentSerializer(instance=tek_ogenci, data=request.data) 
    if serilaizer.is_valid():
        serilaizer.save()
        return Response(serilaizer.data, status=status.HTTP_200_OK)
    return Response(serilaizer.errors, status=status.HTTP_400_BAD_REQUEST)
    


@api_view(['DELETE'])
def ogrenci_sil(request, pk):
    tek_ogrenci = get_object_or_404(Student, id=pk)
    tek_ogrenci.delete()
    data = {"message": "Öğrenci silindi"}
    return Response(data)


#############################################################


#!#################### CLASS BASED VIEWS ########################################

#! APIVIEW

class StudentListCreate(APIView):

    def get(self, request):
        students = Student.objects.all()   # quesyset
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class StudentDetail(APIView):

    def get(self, request, pk):
        # student = Student.objects.get(id=pk)
        student = get_object_or_404(Student, id=pk)
        serializer =StudentSerializer(student)
        return Response(serializer.data)
    
    def put(self, request, pk):
        student = get_object_or_404(Student, id=pk)
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        student = get_object_or_404(Student, id=pk)
        student.delete()
        data = {
            "message": f"Student {student.last_name} deleted successfully"
        }
        return Response(data)
    

#! GENERICAPIView and Mixins
""" #? GenericApıView
# One of the key benefits of class-based views is the way they allow you to compose bits of reusable behavior. REST framework takes advantage of this by providing a number of pre-built views that provide for commonly used patterns.

# GenericAPIView class extends REST framework's APIView class, adding commonly required behavior for standard list and detail views.

#? Mixins
# - ListModelMixin
#     - list method
# - CreateModelMixin
#     - create method
# - RetrieveModelMixin
#     - retrieve method
# - UpdateModelMixin
#     - update method
# - DestroyModelMixin
#     - destroy method 
"""

class StudentGAV(mixins.ListModelMixin, mixins.CreateModelMixin, GenericAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    

class StudentDetailGAV(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, GenericAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    

#! Concrete Views

class StudentCV(ListCreateAPIView):
    # queryset = Student.objects.filter(age=20)
    serializer_class = StudentSerializer
    

    def get_queryset(self):
        if self.request.user.is_staff:
            return Student.objects.all() 
        return Student.objects.filter(age=20)

class StudentDetailCV(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    lookup_field = 'first_name'


    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        data = {
            "message": f"{instance.first_name} deleted."
        }
        return Response(data,status=status.HTTP_204_NO_CONTENT)
    
#! ViewSets

# - Django REST framework allows you to combine the logic for a set of related views in a single class, called a ViewSet. 

# - Typically, rather than explicitly registering the views in a viewset in the urlconf, you'll register the viewset with a router class, that automatically determines the urlconf for you.

# There are two main advantages of using a ViewSet class over using a View class.

#  - Repeated logic can be combined into a single class. In the above example, we only need to specify the queryset once, and it'll be used across multiple views.
#  - By using routers, we no longer need to deal with wiring up the URL conf ourselves.

# Both of these come with a trade-off. Using regular views and URL confs is more explicit and gives you more control. ViewSets are helpful if you want to get up and running quickly, or when you have a large API and you want to enforce a consistent URL configuration throughout.


class StudentModelViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class PathModelViewSet(ModelViewSet):
    queryset = Path.objects.all()
    serializer_class = PathSerializer