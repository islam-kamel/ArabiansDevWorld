from django.shortcuts import get_list_or_404, get_object_or_404
from feed.models import Post
from feed.serializer import PostListSerializer, PostSerializer
from rest_framework.response import Response
from rest_framework.views import APIView


class PostListView(APIView):
    @staticmethod
    def get_queryset():
        return get_list_or_404(Post.objects.all())

    def get(self, request):
        obj = self.get_queryset()
        serializer = PostListSerializer(obj, many=True)
        return Response(serializer.data)


class PostDetailsView(APIView):
    def get_object(self, pk):
        obj = get_object_or_404(Post, pk=pk)
        self.check_object_permissions(self.request, obj)
        return obj

    def get(self, request, slug, pk):
        obj = self.get_object(pk)
        serializer = PostSerializer(obj)
        return Response(serializer.data)
