from django.urls import path
from .views import DealerProfileView, DealerProfileCreateView, DealerListView, NearbyDealerListView

urlpatterns = [
    path('profile/create/', DealerProfileCreateView.as_view(), name= 'dealer-profile-create'),
    path('profile/', DealerProfileView.as_view(), name= 'dealer-profile'),
    path('list/', DealerListView.as_view(), name= 'dealer-list'),
    path('nearby/', NearbyDealerListView.as_view(), name='nearby-dealer-list'),
]