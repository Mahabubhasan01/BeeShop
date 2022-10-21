from django.contrib.auth import views as auth_views

from shop.views import (
    DashboardIndex,
    ItemDetailView,
    ProductDetailView,
    CheckoutView,
    HomeView,
    All_Product,
    OrderSummaryView,
    Register,
    Sign_Out,
    SignIn,
    add_to_cart,
    remove_from_cart,
    remove_single_item_from_cart,
    PaymentView,
    AddCouponView,
    RequestRefundView, Dashboard_finance as Finance,
    dashboard_sales as Sales,
    dashboard_influencer as Influencer,
    user_profile,
    change_password


)
from django.urls import path
app_name = 'shop'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('all_products',All_Product.as_view(),name='all_product'),
    path('dashboard/', DashboardIndex, name='index'),
    path('sales/', Sales, name='sales'),
    path('influencer/', Influencer, name='influencer'),
    path('finance/', Finance, name='finance'),
    path('user_profile/', user_profile, name='user_profile'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('order-summary/', OrderSummaryView.as_view(), name='order-summary'),
    path('product/<slug>/', ItemDetailView.as_view(), name='product'),
    path('product/<slug>/', ProductDetailView.as_view(), name='product_detail'),
    path('add-to-cart/<slug>/', add_to_cart, name='add-to-cart'),
    path('add-coupon/', AddCouponView.as_view(), name='add-coupon'),
    path('remove-from-cart/<slug>/', remove_from_cart, name='remove-from-cart'),
    path('remove-item-from-cart/<slug>/', remove_single_item_from_cart,
         name='remove-single-item-from-cart'),
    path('payment/<payment_option>/', PaymentView.as_view(), name='payment'),
    path('request-refund/', RequestRefundView.as_view(), name='request-refund'),
    path('sign-up/', Register, name='register'),
    path('sign-in/', SignIn, name='signin'),
    path('signout/', Sign_Out, name='signout'),


path('change-password/', change_password, name='change_password'),

    path('reset_password/', auth_views.PasswordResetView.as_view(),
         name='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(),
         name='password_reset_done'),
    path('reset_password/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(),
         name='password_reset_complete'),
]
