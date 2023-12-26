from django.urls import path, include

from rest_framework import routers

from .views import FlightModelViewSet, ReservationModelViewSet


router = routers.DefaultRouter()
router.register("flight", FlightModelViewSet)  # flight/    flight/pk  
router.register("reservation", ReservationModelViewSet)

urlpatterns = [
    path("", include(router.urls))
] 
