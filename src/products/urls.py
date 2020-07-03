from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView

from .views import (
        ProductCreateView,
        ProductDetailView,
        ProductDownloadView,
        ProductListView,
        ProductUpdateView,
        ProductRatingAjaxView,
        VendorListView,
)

urlpatterns = [
    path('', ProductListView.as_view(), name="list"), #products:list
    path('vendor/', RedirectView.as_view(pattern_name='products:list'), name="vendor_list"),
    path('vendor/<vendor_name>/', VendorListView.as_view(), name="vendor_detail"),
    path('<int:pk>/', ProductDetailView.as_view(), name="detail"),
    path('<slug>/', ProductDetailView.as_view(), name="detail_slug"),
    path('<int:pk>/download/', ProductDownloadView.as_view(), name="download"),
    path('<slug>/download/', ProductDownloadView.as_view(), name="download_slug"),
    path('<int:pk>/edit/', ProductUpdateView.as_view(), name="update"),
    path('<slug>/edit/', ProductUpdateView.as_view(), name="update_slug"),
    path('ajax/rating/', ProductRatingAjaxView.as_view(), name="ajax_rating"),


]
