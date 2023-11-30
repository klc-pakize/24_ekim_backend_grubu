from django.urls import path, include

from .views import home, butun_ogrencileri_getir, yeni_ogreci_create_et, tek_ogrenciyi_goruntuleme_islemi, qorenciyi_guncelle, ogrenci_sil

urlpatterns = [
    path("homesayfasinigetir/", home),
    path("ogrecilerinhepsinigetir/", butun_ogrencileri_getir),
    path("yeniogrenciolustur/", yeni_ogreci_create_et),
    path("tekogrenci/<int:pk>/", tek_ogrenciyi_goruntuleme_islemi),
    path("ogrencigüncelle/<int:pk>/", qorenciyi_guncelle),
    path("ogrencisil/<int:pk>/", ogrenci_sil )
]
