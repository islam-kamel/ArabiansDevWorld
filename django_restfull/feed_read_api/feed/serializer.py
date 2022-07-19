from feed.models import Post
from rest_framework import serializers
from user.serializers import UserShortSerializer


class PostSerializer(serializers.ModelSerializer):
    """posts custom serializer with include tags and some user information"""

    # post_tags = TagsSerializer(many=True, read_only=True)
    # post_comments = CommentSerializer(many=True, read_only=True)
    user = UserShortSerializer(read_only=True)
    slug = serializers.SlugField(required=False)

    class Meta:
        model = Post
        fields = [
            "pk",
            "title",
            "content",
            "slug",
            # "post_tags",
            "published_at",
            "update_at",
            "status",
            "user",
            # "post_comments",
        ]

    def create(self, validated_data):
        title = validated_data.get("title")
        post = Post.objects.create(**validated_data, slug=title.replace(" ", "-"))
        return post


class PostListSerializer(serializers.ModelSerializer):
    """Post list serializer with limit data to optimize response"""

    user = UserShortSerializer(read_only=True)
    # user = serializers.StringRelatedField(read_only=True)
    post_comments = Post.get_total_comments

    class Meta:
        model = Post
        # fields = ['__all__']
        fields = [
            "pk",
            "title",
            "published_at",
            "slug",
            "user",
            # "post_comments",
        ]
