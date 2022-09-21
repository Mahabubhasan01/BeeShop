from django.urls import path
from .views import HomeView,CheckoutView
app_name = 'shop'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
]
