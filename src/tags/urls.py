from django.contrib import admin
from django.urls import path, include

from .views import (
    TagDetailView,
    TagListView
)

urlpatterns = [
    path('', TagListView.as_view(), name="list"),
    path('<slug>/', TagDetailView.as_view(), name="detail"),

]
