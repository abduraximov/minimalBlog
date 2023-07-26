from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            "id",
            "title",
            "slug",
            "description",
            "photo",
            "content",
            "author",
            "category",
            "tags",
            "video",
            "views_count",
            "is_popular"
        )


class PostDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            "id",
            "title",
            "description",
            "photo",
            "content",
            "author",
            "category",
            "tags",
            "video",
            "views_count",
            "is_popular"
        )


