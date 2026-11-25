from django.urls import path
from .views import RegisterView, ProfileView, DealerTestView, CustomerTestView, BusinessTestView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('dealer-test/', DealerTestView.as_view(), name='dealer-test'),
    path('customer-test/', CustomerTestView.as_view(), name='customer-test'),
    path('business-test/', BusinessTestView.as_view(), name='business-test')
]
