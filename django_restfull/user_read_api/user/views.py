from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from user.serializers import UserSerializer

user_model = get_user_model()


# View data specific user
class UserDetailsView(APIView):
    def get_object(self, username):
        obj = get_object_or_404(user_model, username=username)
        self.check_object_permissions(self.request, obj)
        return obj

    def get(self, request, username):
        obj = self.get_object(username)
        serializer = UserSerializer(obj, context={"request": request})
        return Response(serializer.data, status=status.HTTP_200_OK)
