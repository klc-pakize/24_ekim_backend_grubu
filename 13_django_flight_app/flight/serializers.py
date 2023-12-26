from rest_framework import serializers

from .models import Flight, Reservation, Passenger


class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = "__all__"
        read_only_fileds = ["id"]


class PassengerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passenger
        fields = "__all__"
        read_only_fileds = ["id"]


class ReservationSerializer(serializers.ModelSerializer):
    passenger = PassengerSerializer(many=True)
    flight = serializers.StringRelatedField()  # read_only
    flight_id = serializers.IntegerField()
    user = serializers.StringRelatedField()  # read_only
    # user_id = serializers.IntegerField()

    class Meta:
        model = Reservation
        fields = "__all__"
        read_only_fileds = ["id"]


# validated_data = {
#     "passenger": [
#         {
#             "first_name": "Furkan",
#             "last_name": "Kılıç",
#             "email": "pa3kize@gmail.com",
#             "phone_number": 322,
#             "update_date": "2023-12-26T17:59:36.032083Z",
#             "create_date": "2023-12-26T17:59:36.032083Z"
#         },
#         {
#             "first_name": "Ali",
#             "last_name": "KILIÇ",
#             "email": "nisanurklc054@gmail.com",
#             "phone_number": 2131,
#             "update_date": "2023-12-26T17:59:54.092202Z",
#             "create_date": "2023-12-26T17:59:54.092202Z"
#         }
#     ],
#     "flight_id": 2,
#     "user_id": 2
# }
    
    def create(self, validated_data):
        passenger_data = validated_data.pop('passenger')

        validated_data['user_id'] = self.context['request'].user.id
        revervation = Reservation.objects.create(**validated_data)

        for passenger in passenger_data:
            pas = Passenger.objects.create(**passenger)

            revervation.passenger.add(pas)

        revervation.save()
        return revervation
    


class StaffFlightSerializer(serializers.ModelSerializer):
    flight_reservation = ReservationSerializer(many=True, read_only=True)
    class Meta:
        model = Flight
        fields = "__all__"
        read_only_fileds = ["id"]