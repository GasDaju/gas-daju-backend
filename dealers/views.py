from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from accounts.permissions import IsDealer, IsCustomer
from .models import DealerProfile
from .serializers import DealerProfileSerializer, DealerListSerializer
from math import radians, sin, cos, sqrt, atan2
from rest_framework.exceptions import ValidationError

def calculate_distance(lat1, lon1, lat2, lon2):
    earth_radius = 6371

    lat1, lon1, lat2, lon2= map(
        radians, [lat1, lon1, lat2, lon2]
    ) 

    dlat = lat2-lat1
    dlon= lon2-lon1

    a=(
        sin(dlat/2)**2
        + cos(lat1)* cos(lat2)*sin(dlon/2)**2
    )

    c= 2* atan2(sqrt(a), sqrt(1-a))
    return earth_radius*c


class DealerProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = DealerProfileSerializer
    permission_classes = [IsAuthenticated, IsDealer]

    def get_object(self):
        return DealerProfile.objects.get(user= self.request.user)

class DealerListView(generics.ListAPIView):
    serializer_class= DealerListSerializer
    permission_classes= [IsAuthenticated, IsCustomer]

    def get_queryset(self):
        queryset= DealerProfile.objects.all()

        city = self.request.query_params.get('city')

        if city:
            queryset= queryset.filter(city__icontains=city)

        return queryset

class NearbyDealerListView(generics.ListAPIView):
    serializer_class= DealerListSerializer
    permission_classes= [IsAuthenticated, IsCustomer]

    def get_queryset(self):
        latitude = self.request.query_params.get('latitude')
        longitude= self.request.query_params.get('longitude')
        radius= self.request.query_params.get('radius', 5)

        if latitude is None or longitude is None:
            raise ValidationError(
                'Latitude and longitude are required.'
            )
        try: 
            latitude= float(latitude)
            longitude= float(longitude)
            radius= float(radius)

        except ValueError:
            raise ValidationError("Invalid location or radius.")

        if not (-90 <= latitude <= 90):
            raise ValidationError("Invalid latitude.")

        if not (-180 <= longitude <= 180):
            raise ValidationError("Invalid longitude.")

        if radius <= 0:
            raise ValidationError("Radius must be greater than zero.")

        dealers = DealerProfile.objects.exclude(
            latitude__isnull=True
        ).exclude(
            longitude__isnull=True
        )

        nearby_dealers = []

        for dealer in dealers:
            distance = calculate_distance(
                latitude,
                longitude,
                float(dealer.latitude),
                float(dealer.longitude)
            )

            if distance <= radius:
                nearby_dealers.append((dealer, distance))

        nearby_dealers.sort(key=lambda item: item[1])

        return [dealer for dealer, distance in nearby_dealers]

    
class DealerProfileCreateView(generics.CreateAPIView):
    serializer_class = DealerProfileSerializer
    permission_classes = [IsAuthenticated, IsDealer]

    def perform_create(self, serializer):
        serializer.save(user = self.request.user)
        
# Create your views here.
