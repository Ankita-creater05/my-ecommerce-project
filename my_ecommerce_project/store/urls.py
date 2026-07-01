from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('add-to-wishlist/<int:product_id>/', views.add_to_wishlist, name='add_to_wishlist'),
    path('product/<int:product_id>/add-review/', views.add_review, name='add_review'),
    path('cart/', views.cart_view, name='cart'),
    path('wishlist/', views.wishlist_view, name='wishlist'),
    path('login/', views.login_view, name='login'), 
    path('login/', auth_views.LoginView.as_view(template_name='store/login.html'), name='login'),
]