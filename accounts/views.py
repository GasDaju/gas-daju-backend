from .permissions import IsDealer, IsCustomer, IsBusiness
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import RegisterSerializer

class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

class ProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({
            "username": request.user.username,
            "email": request.user.email,
            "phone_number": request.user.phone_number,
            "role": request.user.role
        })

class DealerTestView(APIView):
    permission_classes = [IsDealer]

    def get(self, request):
        return Response({
            "message": "Welcome Dealer!",
            "username": request.user.username,
            "role": request.user.role
        })

class CustomerTestView(APIView):
    permission_classes = [IsCustomer]

    def get(self, request):
        return Response({
            "message": "Welcome Customer!",
            "username": request.user.username,
            "role": request.user.role
        })

class BusinessTestView(APIView):
    permission_classes = [IsBusiness]

    def get(self, request):
        return Response({
            "message": "Welcome Business User!",
            "username": request.user.username,
            "role": request.user.role
        })