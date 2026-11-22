from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ValidationError

from accounts.permissions import IsCustomer, IsDealer
from .models import Order
from .serializers import OrderSerializer


class CustomerOrderListCreateView(generics.ListCreateAPIView):
    serializer_class= OrderSerializer
    permission_classes= [IsAuthenticated, IsCustomer]

    def get_queryset(self):
        return Order.objects.filter(
            customer= self.request.user
        )

    def perform_create(self, serializer):
        inventory= serializer.validated_data['inventory']
        quantity= serializer.validated_data['quantity']

        if not inventory.is_available or inventory.available_quantity <=0:
            raise ValidationError("This inventory is currently unavailable.")

        if quantity > inventory.available_quantity:
            raise ValidationError(
                "Requested quantity exceeds available stock."
            )

        serializer.save(
            customer= self.request.user,
            dealer= inventory.dealer
        )

class DealerOrderListView(generics.ListAPIView):
    serializer_class= OrderSerializer
    permission_classes= [IsAuthenticated, IsDealer]

    def get_queryset(self):
        return Order.objects.filter(
            dealer__user= self.request.user
        )