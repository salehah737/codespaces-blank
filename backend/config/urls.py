from django.contrib import admin # type: ignore
from django.urls import path, include # type: ignore
from django.urls import path # type: ignore
from .views import RegisterView, LoginView # type: ignore

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('users.urls')),
    path('api/ecommerce/', include('ecommerce.urls')),
    path('api/inventory/', include('inventory.urls')),
    path('api/franchises/', include('franchises.urls')),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
]