from django.urls import path
from django.views.decorators.cache import cache_page
from django.views.generic import TemplateView

from . import views


urlpatterns = [
    path('comment/<int:pk>/', views.CreateComment.as_view(), name="create_comment"),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name="about"),
    path('cart/', views.cart, name="cart"),
    path('<slug:slug>/<slug:product_slug>/', views.ProductDetailView.as_view(), name="product_detail"),
    path('<slug:slug>/', views.ProductListView.as_view(), name="product_list"),
    path('',views.HomeView.as_view(), name="index"),
    path('add-item-to-cart/<int:pk>', views.add_item_to_cart, name='add_item_to_cart'),
    path('delete_item/<int:pk>', views.CartDeleteItem.as_view(), name='cart_delete_item'),
]