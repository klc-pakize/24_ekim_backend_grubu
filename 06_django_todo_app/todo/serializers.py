from rest_framework import serializers

from .models import Todo


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        # fields = (
        #     'id',  # read_only
        #     'task', 
        #     'description', 
        #     'priority', 
        #     'is_done', 
        #     'create_date',  # read_only
        #     'update_date'  # read_only
        # )
        fields = "__all__"
        read_only_fields = ["id"]
