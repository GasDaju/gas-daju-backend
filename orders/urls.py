from django.urls import path
from .views import (
    CustomerOrderListCreateView,
    DealerOrderListView,
)

urlpatterns = [
    path('customer/', CustomerOrderListCreateView.as_view(), name='customer-orders'),
    path('dealer/', DealerOrderListView.as_view(), name='dealer-orders'),
]