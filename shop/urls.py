from django.urls import path
from .views import *




urlpatterns = [
    path('', IndexView.as_view()),
    path('shop/', ShopView.as_view(), name='shop'),
    path('shop/<int:page_id>', ShopView.as_view()),
    path('about/', AboutView.as_view(), name='about'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('blog/', BlogView.as_view(), name='blog'),
    path('blog-single/<int:pk>', BlogSingleView.as_view(), name='blog-single'),
    path('wishlist/', WishlistView.as_view(), name='wishlist'),
    path('product-single/', ProductSingleView.as_view(), name='product-single'),
    path('cart/', CartView.as_view(), name='cart'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
]
