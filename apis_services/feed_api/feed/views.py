from django.shortcuts import get_list_or_404, get_object_or_404
from drf_yasg.utils import swagger_auto_schema
from feed.models import Post
from feed.serializer import (
    PostCreateSerializer,
    PostListSerializer,
    PostUpdateSerializer,
)
from logging_manager import eventslog
from permissions.permissions import IsOwnerOrReadOnly
from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView

logger = eventslog.logger


class PostListView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    @staticmethod
    def get_queryset():
        return get_list_or_404(Post.objects.all())

    @swagger_auto_schema(operation_summary="List all posts")
    def get(self, request):
        obj = self.get_queryset()
        serializer = PostListSerializer(obj, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_summary="Create new post", request_body=PostCreateSerializer
    )
    def put(self, request):
        request.data["user_id"] = request.user.id
        serializer = PostCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.create(serializer.validated_data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        logger.error(f"{serializer.errors} - {request.user}")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostDetailsView(APIView):
    permission_classes = [IsOwnerOrReadOnly]

    def get_object(self, pk):
        obj = get_object_or_404(Post, pk=pk)
        self.check_object_permissions(self.request, obj)
        return obj

    @swagger_auto_schema(operation_summary="Get specific post by {slug, id}")
    def get(self, request, pk, **kwargs):
        obj = self.get_object(pk)
        serializer = PostCreateSerializer(obj)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_summary="Update specific post by {slug, id}",
        request_body=PostUpdateSerializer,
    )
    def put(self, request, pk, **kwargs):
        serializer = PostUpdateSerializer(data=request.data)
        obj = self.get_object(pk)
        if serializer.is_valid():
            serializer.update(obj, serializer.validated_data)
            return Response(serializer.data)
        logger.error(f"{serializer.errors} - {request.user}")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(operation_summary="Delete specific post by {slug, id}")
    def delete(self, request, pk, **kwargs):
        obj = self.get_object(pk)
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
