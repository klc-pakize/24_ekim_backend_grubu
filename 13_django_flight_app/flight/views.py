from datetime import datetime, date

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Flight, Reservation
from .serializers import FlightSerializer, ReservationSerializer, StaffFlightSerializer
from .permissions import IsStaffOrReadOnly


class FlightModelViewSet(viewsets.ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer
    permission_classes = [IsStaffOrReadOnly]

    def get_queryset(self):
        now = datetime.now()
        current_time = now.strftime('%H:%M:%S')
        today = date.today()

        if self.request.user.is_staff:
            return super().get_queryset()
        
        else:
            queryset = Flight.objects.filter(date_of_departure__gt=today)

            if Flight.objects.filter(date_of_departure=today):
                today_gueryset = Flight.objects.filter(estimated_timeof_departure__gt=current_time)

                queryset = queryset.union(today_gueryset)
            
            return queryset

    def get_serializer_class(self):
        serializer = super().get_serializer_class()
        # serializer = FlightSerializer

        if self.request.user.is_staff:
            return StaffFlightSerializer
        
        return serializer


class ReservationModelViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    permission_classes = [IsAuthenticated]


    def get_queryset(self):
        # queryset = Reservation.objects.all()
        queryset = super().get_queryset()

        # user = self.request.user

        if self.request.user.is_staff:
            return queryset
        
        # return Reservation.objects.filter(user=self.request.user)
        return queryset.filter(user=self.request.user)