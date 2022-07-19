import django.db.utils
from django.contrib.auth import get_user_model

from user.serializers import CreateUserSerializer, UserSerializer

model = get_user_model()

tags_list = [
    "python",
    "djagno",
    "javaScript",
    "C",
    "C++",
    "C#",
    "Haskl",
    "Pascal",
    "Rust",
    "Rube",
    "Go",
    "Scala",
]


def create_user():
    for i in range(3, 100000000):
        data = {
            "username": f"test_user_{i}",
            "email": f"test@mail{i}.com",
            "date_of_birth": "1999-7-13",
            "password": "123",
        }
        try:
            serializer = CreateUserSerializer(data=data)
            if serializer.is_valid():
                serializer.create(serializer.validated_data)
            user = model.objects.get(username=data["username"])
        except django.db.utils.IntegrityError:
            continue

        update = {
            "name": {
                "first_name": f"test_user_{i}",
                "last_name": f"Kamel{i}",
                "user_id": user.pk,
            },
            "bio": {"bio": "hello Friend", "user_id": user.pk},
            "skills": {"skill": "Python,docker,c,", "user_id": user.pk},
            "github_url": {
                "url": "https://www.github.com/user/",
                "user_id": user.pk,
            },
            "phone": {"phone": "01066373279", "user_id": user.pk},
            "address": {
                "country": "Egypt",
                "city": "Qena",
                "street_name": "Qus",
                "user_id": user.pk,
            },
        }

        serializer = UserSerializer(data=update)
        if serializer.is_valid():
            serializer.update(
                instance=user, validated_data=serializer.validated_data
            )

            print(
                f"Create Done ID --> {user.id} username --> {user.username})"
            )
            print("-" * 50)
