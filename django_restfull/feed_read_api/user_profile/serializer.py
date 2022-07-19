from rest_framework import serializers

from .models import Name


class NameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Name
        fields = ["first_name", "last_name"]
