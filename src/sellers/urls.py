from django.contrib import admin
from django.urls import path, include

from .views import (
        SellerDashboard,
)

urlpatterns = [
    path('', SellerDashboard.as_view(), name="dashboard"),
]
