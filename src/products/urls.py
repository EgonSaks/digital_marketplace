from django.contrib import admin
from django.urls import path, include

from .views import (
        ProductCreateView,
        ProductDetailView,
        ProductListView,
        ProductUpdateView,
)

urlpatterns = [
    path('', ProductListView.as_view(), name="list"),
    path('add/', ProductCreateView.as_view(), name="create"),
    path('<int:pk>/', ProductDetailView.as_view(), name="detail"),
    path('<slug>/', ProductDetailView.as_view(), name="detail_slug"),
    path('<int:pk>/edit/', ProductUpdateView.as_view(), name="update"),
    path('<slug>/edit/', ProductUpdateView.as_view(), name="update_slug"),
]
