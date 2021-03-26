from rest_framework import serializers
from .models import todos

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = todos
        fields = ("id","completed","content","date_created","due_date")
