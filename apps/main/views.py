from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Contact
from .serializer import ContactSerializer


class ContactsApiView(APIView):
    def post(self, request):
        contact = Contact.objects.all()
        serializer = ContactSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=201)

