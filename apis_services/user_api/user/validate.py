import re

from rest_framework import serializers


def validate_username(username):
    # Pattern xxxx.xxxx or xxxx_xxxx
    pattern = re.compile(r"^[a-zA](?=[a-zA-Z\d._]{8,20}$)(?!.*[_.]{2})[^_.].*[^_.]$")
    if re.fullmatch(pattern, username):
        return username
    raise serializers.ValidationError("Enter valid username ex. xxxx.xxxx or xxxx_xxxx")


def validate_skills(skills):
    # Pattern python,django or python
    pattern = re.compile(r"^([aA-zZ]+)$|^(([aA-zZ]+),([aA-zZ]+))+$")
    if re.fullmatch(pattern, skills):
        return skills
    raise serializers.ValidationError("Enter valid skills ex. python or python,...")
