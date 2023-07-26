from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Post
from .serializer import PostSerializer


class PostApiView(APIView):

    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data, status=200)
#
#
# class PostDetailApiView(APIView):
#
