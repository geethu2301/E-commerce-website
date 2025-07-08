from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('product/<int:id>/', views.product_detail, name='product_detail'),
    path('cart/', views.cart, name='cart'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('orders/', views.orders, name='orders'),
]
