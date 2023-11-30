from django.shortcuts import render, HttpResponse, get_object_or_404

from .models import Student, Path

from .serializers import StudentSerializer, PathSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET'])
def home(request):
    return Response({"home": "This is home page..."})


# http methods ----------->
# - GET (DB den veri çağırma, public)
# - POST(DB de değişklik, create, private)
# - PUT (DB DE KAYIT DEĞİŞKLİĞİ, private)
# - delete (dB de kayıt silme)
# - patch (kısmi update)


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