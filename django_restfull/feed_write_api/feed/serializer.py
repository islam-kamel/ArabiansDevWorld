from feed.models import Post
from rest_framework import serializers


class PostCreateSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(required=True)
    slug = serializers.SlugField(required=False)

    class Meta:
        model = Post
        fields = [
            "pk",
            "title",
            "content",
            "slug",
            "published_at",
            "update_at",
            "status",
            "user_id",
        ]

    def create(self, validated_data):
        title = validated_data.get("title")
        post = Post.objects.create(**validated_data, slug=title.replace(" ", "-"))
        return post


class PostUpdateSerializer(serializers.ModelSerializer):
    """Post serializer for only update post date"""

    title = serializers.CharField(required=False)
    content = serializers.CharField(required=False)

    class Meta:
        model = Post
        fields = ["title", "content"]

    def update(self, instance, validated_data):
        instance.title = validated_data.get("title", instance.title)
        instance.content = validated_data.get("content", instance.content)
        instance.save()
        return instance
