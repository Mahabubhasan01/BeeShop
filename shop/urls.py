
from django.urls import path
app_name = 'shop'

from shop.views import (
    DashboardIndex,
    ItemDetailView,
    CheckoutView,
    HomeView,
    OrderSummaryView,
    add_to_cart,
    remove_from_cart,
    remove_single_item_from_cart,
    PaymentView,
    AddCouponView,
    RequestRefundView,Dashboard_finance as Finance,
    dashboard_sales as Sales,
    dashboard_influencer as Influencer
    
)
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('dashboard/', DashboardIndex, name='index'),
    path('sales/', Sales, name='sales'),
    path('influencer/', Influencer, name='influencer'),
    path('finance/', Finance, name='finance'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('order-summary/', OrderSummaryView.as_view(), name='order-summary'),
    path('product/<slug>/', ItemDetailView.as_view(), name='product'),
    path('add-to-cart/<slug>/', add_to_cart, name='add-to-cart'),
    path('add-coupon/', AddCouponView.as_view(), name='add-coupon'),
    path('remove-from-cart/<slug>/', remove_from_cart, name='remove-from-cart'),
    path('remove-item-from-cart/<slug>/', remove_single_item_from_cart,
         name='remove-single-item-from-cart'),
    path('payment/<payment_option>/', PaymentView.as_view(), name='payment'),
    path('request-refund/', RequestRefundView.as_view(), name='request-refund')
]
