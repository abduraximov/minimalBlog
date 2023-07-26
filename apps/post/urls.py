from django.urls import path
from .views import PostApiView, PostDetailView

urlpatterns = [
    path("", PostApiView.as_view(), name="posts"),
    path("detail/<slug:slug>", PostDetailView.as_view(), name="detail")
]