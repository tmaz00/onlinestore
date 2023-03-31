from django.urls import path
from . import views


urlpatterns = [
    path("", views.store, name='home'),
    path('products/<int:id>/', views.product_detail, name='product-detail'),
    path('filter/', views.filter_products, name='filter'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name="checkout"),
    path('update_item', views.update_item, name='update_item'),
]