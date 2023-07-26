from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Post
from .serializer import PostSerializer, PostDetailSerializer


class PostApiView(APIView):

    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data, status=200)


class PostDetailView(APIView):
    def get(self, request, slug):
        post = Post.objects.get(slug=slug)
        serializer = PostDetailSerializer(post)
        return Response(serializer.data, status=200)

