from django.urls import path
from .views import InventoryListCreateView, InventoryDetailView, CustomerInventoryListView

urlpatterns = [
    path('', InventoryListCreateView.as_view(), name= 'inventory-list-create'),
    path('<int:pk>/', InventoryDetailView.as_view(), name= 'inventory-detail'),
    path('customer/', CustomerInventoryListView.as_view(), name='customer-inventory-list'),
]