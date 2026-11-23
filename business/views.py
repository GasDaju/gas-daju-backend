from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def business_home(request):
    return Response({
        "message": "Welcome to Gas Daju Business API!",
        "status": "Business module is working successfully"
    })