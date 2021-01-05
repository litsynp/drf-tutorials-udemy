from django.contrib import admin
from django.urls import path

from .views import UpdateModelDetailAPIView, UpdateModelListAPIView

urlpatterns = [
    # api/updates/ - List/Create
    path('', UpdateModelListAPIView.as_view()),

    # api/updates/1/ - Retrieve, Update, Delete
    path('<int:id>', UpdateModelDetailAPIView.as_view()),
]
