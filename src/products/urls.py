from django.contrib import admin
from django.urls import path, include

from .views import (
        ProductCreateView,
        ProductDetailView,
        ProductDownloadView,
        ProductListView,
        ProductUpdateView,
)

urlpatterns = [
    path('', ProductListView.as_view(), name="list"), #products:list
    path('<int:pk>/', ProductDetailView.as_view(), name="detail"),
    path('<slug>/', ProductDetailView.as_view(), name="detail_slug"),
    path('<int:pk>/download/', ProductDownloadView.as_view(), name="download"),
    path('<slug>/download/', ProductDownloadView.as_view(), name="download_slug"),
    path('<int:pk>/edit/', ProductUpdateView.as_view(), name="update"),
    path('<slug>/edit/', ProductUpdateView.as_view(), name="update_slug"),
]
