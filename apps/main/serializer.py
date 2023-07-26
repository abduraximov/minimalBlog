from rest_framework import serializers
from apps.main.models import Contact


class ContactSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contact
        fields = (
            "id",
            "name",
            "subject",
            "text",
            "email"
        )
