from django.contrib.auth import get_user_model
from rest_framework import serializers
from user_profile.serializer import NameSerializer


class UserShortSerializer(serializers.ModelSerializer):
    name = NameSerializer(read_only=True)

    class Meta:
        model = get_user_model()
        fields = ["pk", "username", "name"]
