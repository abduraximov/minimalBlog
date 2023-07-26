from django.urls import path
from .views import ContactsApiView


urlpatterns = [
    path('contacts/', ContactsApiView.as_view(), name="contact")
]