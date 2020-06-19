from django.contrib import admin
from django.urls import path, include

from .views import (
        SellerDashboard,
        SellerTransactionListView
)

urlpatterns = [
    path('', SellerDashboard.as_view(), name="dashboard"),
    path('transactions/', SellerTransactionListView.as_view(), name="transactions"),
]
