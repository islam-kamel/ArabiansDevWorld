import re

from django.contrib.auth import get_user_model
from rest_framework import serializers
from user.validate import validate_skills, validate_username


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=False)
    date_of_birth = serializers.DateField(required=False)
    username = serializers.CharField(required=False, validators=[validate_username])
    skills = serializers.CharField(required=False, validators=[validate_skills])

    class Meta:
        model = get_user_model()
        fields = [
            "id",
            "username",
            "full_name",
            "email",
            "date_of_birth",
            "join_date",
            "bio",
            "skills",
            "github",
            "phone",
        ]

    # @staticmethod
    # def validate_username(username):
    #     # Pattern xxxx.xxxx or xxxx_xxxx
    #     pattern = re.compile(
    #         r"^[a-zA](?=[a-zA-Z\d._]{8,20}$)(?!.*[_.]{2})[^_.].*[^_.]$"
    #     )
    #     if re.fullmatch(pattern, username):
    #         return username
    #     raise serializers.ValidationError("Enter valid username ex. xxxx.xxxx or xxxx_xxxx")
    #
    #
    # @staticmethod
    # def validate_skills(skills):
    #     # Pattern python,django or python
    #     pattern = re.compile(
    #         r"^([aA-zZ]+)$|^(([aA-zZ]+),([aA-zZ]+))+$"
    #     )
    #     if re.fullmatch(pattern, skills):
    #         return skills
    #     raise serializers.ValidationError("Enter valid skills ex. python or python,...")


class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ["username", "full_name", "email", "date_of_birth", "password"]
        extra_kwargs = {"password": {"write_only": True, "required": True}}

    @staticmethod
    def validate_username(username):
        pattern = re.compile(
            r"^[a-zA](?=[a-zA-Z\d._]{8,20}$)(?!.*[_.]{2})[^_.].*[^_.]$"
        )
        if re.fullmatch(pattern, username):
            return username
        raise serializers.ValidationError("Enter valid username ex. xxxx.xxxx")

    #
    # def create(self, validated_data):
    #     user = get_user_model()
    #     user.objects.create_user(**validated_data)
    #     return user
