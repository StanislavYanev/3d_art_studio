from django.urls import path
from .views import GalleryView, GalleryDetailView

app_name = "gallery"

urlpatterns = [
    path('', GalleryView.as_view(), name='gallery'),



]
