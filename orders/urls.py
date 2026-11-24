from django.urls import path
from .views import (
    CustomerOrderListCreateView,
    DealerOrderListView,
    DealerOrderStatusUpdateView
)

urlpatterns = [
    path('customer/', CustomerOrderListCreateView.as_view(), name='customer-orders'),
    path('dealer/', DealerOrderListView.as_view(), name='dealer-orders'),
    path('dealer/<int:pk>/status/',
         DealerOrderStatusUpdateView.as_view(),
         name= 'dealer-order-status-updtae'
        ),

]