from django.utils.timezone import now

from rest_framework import serializers

from .models import Departman, Personel


class DepartmanSerializer(serializers.ModelSerializer):

    personel_count = serializers.SerializerMethodField()

    class Meta:
        model = Departman
        fields = "__all__"
        # fields = ("id", "name")
        read_only_fields = ["id"]
    
    def get_personel_count(self, departman_object):
        return departman_object.personel_set.count()
    
    # departman = models.ForeignKey(Departman, on_delete=models.CASCADE, related_name="personels")
        # return departman_object.personels.count()
    

class PersonelSerializer(serializers.ModelSerializer):

    days_since_joined = serializers.SerializerMethodField()  # read_only
    departman = serializers.StringRelatedField() # read_only
    departman_id = serializers.IntegerField()
    class Meta:
        model = Personel
        fields = "__all__"
        read_only_fields = ["id", "user"]

    def get_days_since_joined(self, personel_object):
        return (now() - personel_object.start_date).days

    def create(self, validated_data):
        validated_data["user"] = self.context['request'].user
        personel = Personel.objects.create(**validated_data)
        return personel