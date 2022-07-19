from django.contrib.auth import get_user_model
from logging_manager import eventslog
from rest_framework import serializers
from user_profile.serializer import NameSerializer

logger = eventslog.logger


class UserShortSerializer(serializers.ModelSerializer):
    name = NameSerializer(read_only=True)

    class Meta:
        model = get_user_model()
        fields = ["pk", "name"]
