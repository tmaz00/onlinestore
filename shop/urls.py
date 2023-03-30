from django.urls import path
from . import views


urlpatterns = [
    path("", views.ProductListView.as_view(), name='home'),
    path('products/<int:pk>/', views.ProductDetailView.as_view(), name='product-detail'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name="checkout"),
]