from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from accounts.permissions import IsDealer, IsCustomer
from .models import Inventory
from .serializers import InventorySerializer


class InventoryListCreateView(generics.ListCreateAPIView):
    serializer_class = InventorySerializer
    permission_classes = [IsAuthenticated, IsDealer]

    def get_queryset(self):
        return Inventory.objects.filter(dealer__user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(dealer=self.request.user.dealer_profile)


class InventoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = InventorySerializer
    permission_classes = [IsAuthenticated, IsDealer]

    def get_queryset(self):
        return Inventory.objects.filter(dealer__user=self.request.user)

class CustomerInventoryListView(generics.ListAPIView):
    serializer_class = InventorySerializer
    permission_classes= [IsAuthenticated, IsCustomer]

    def get_queryset(self):
        return Inventory.objects.filter(
            is_available = True,
            available_quantity__gt= 0
        )