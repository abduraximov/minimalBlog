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
            "is_popular"
        )


class PostDetailSerializer(serializers.ModelSerializer):
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
            "is_popular"
        )

    def save(self, **kwargs):
        pass


