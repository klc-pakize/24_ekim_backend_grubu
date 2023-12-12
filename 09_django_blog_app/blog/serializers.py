from rest_framework import serializers

from .models import Category, Blog


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"
        read_only_fields = ["id"]



class BlogSerializer(serializers.ModelSerializer):
    cotegory = serializers.StringRelatedField()  # read_only
    cotegory_id = serializers.IntegerField()

    class Meta:
        model = Blog
        fields = "__all__"
        read_only_fields = ["id", "created_date", "updated_date"]