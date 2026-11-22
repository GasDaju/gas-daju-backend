from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from accounts.permissions import IsDealer
from .models import DealerProfile
from .serializers import DealerProfileSerializer

class DealerProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = DealerProfileSerializer
    permission_classes = [IsAuthenticated, IsDealer]

    def get_object(self):
        return DealerProfile.objects.get(user= self.request.user)

class DealerProfileCreateView(generics.CreateAPIView):
    serializer_class = DealerProfileSerializer
    permission_classes = [IsAuthenticated, IsDealer]

    def perform_create(self, serializer):
        serializer.save(user = self.request.user)
        
# Create your views here.
