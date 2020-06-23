from django.contrib import admin
from django.urls import path, include

from products.views import (
        ProductUpdateView,
        ProductCreateView,
        SellerProductListView
)

from .views import (
        SellerDashboard,
        SellerTransactionListView
)

urlpatterns = [
    path('', SellerDashboard.as_view(), name="dashboard"),
    path('transactions/', SellerTransactionListView.as_view(), name="transactions"),
    path('products/', SellerProductListView.as_view(), name="product_list"),#sellers:product_list
    path('<int:pk>/edit/', ProductUpdateView.as_view(), name="product_edit"),
    path('products/add/', ProductCreateView.as_view(), name="product_create"),
]
