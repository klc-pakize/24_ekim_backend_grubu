from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from django.contrib.auth.models import User


class RegisterSerializer(serializers.ModelSerializer):

    email = serializers.EmailField(required=True, validators=[UniqueValidator(queryset=User.objects.all())])
    password = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ("id", "first_name", "last_name", "username", "email", "password", "password2")


    # Frontend gelen veri
    # attrs = {
    #     "firts_name": "",
    #     "last_name": "",
    #     "username": "",
    #     "email": "",
    #     "password": "",
    #     "password2": "",
    # }

    # def validate(self, data):
    #     return super().validate(data)

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"error":"Password fields didnt match.!!!"})
        return attrs
    
    # validated_data = {
    #     "firts_name": "",
    #     "last_name": "",
    #     "username": "",
    #     "email": "",
    #     "password": "",
    #     "password2": "",
    # }

    def create(self, validated_data):
        validated_data.pop("password2")
        password = validated_data.pop("password")
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        return user