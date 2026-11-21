from django.urls import path
from .views import RegisterView, ProfileView, DealerTestView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('dealer-test/', DealerTestView.as_view(), name='dealer-test'),
]
