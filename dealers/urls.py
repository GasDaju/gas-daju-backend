from django.urls import path
from .views import DealerProfileView, DealerProfileCreateView

urlpatterns = [
    path('profile/create/', DealerProfileCreateView.as_view(), name= 'dealer-profile-create'),
    path('profile/', DealerProfileView.as_view(), name= 'dealer-profile'),
]