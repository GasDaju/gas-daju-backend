
from django.contrib import admin
from django.urls import path, include

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),

    # JWT authentication
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Core API
    path('api/', include('core.urls')),

    # Business customer API
    path('api/business/', include('business.urls')),

    # Shared Gas Daju APIs
    path('api/accounts/', include('accounts.urls')),
    path('api/dealers/', include('dealers.urls')),
    path('api/inventory/', include('inventory.urls')),
    path('api/orders/', include('orders.urls')),
]
