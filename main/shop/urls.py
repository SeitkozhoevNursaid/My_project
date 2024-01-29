from django.urls import path
from .views import PostView, AddToCartView
from .views import *

urlpatterns = [
    path('',PostView.as_view(), name = 'shop'),
    path('category',SecondView.as_view()),
    path('cart/', view_cart, name='view_cart'),
    path('add_to_cart/<int:product_id>/', AddToCartView.as_view(), name='add_to_cart'),
]

