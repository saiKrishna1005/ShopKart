from django.urls import path,include
from . import views
from .views import *

urlpatterns = [
    path('',views.home.as_view(),name="home"),
    path('register/',views.register,name="register"),
    path('login',views.login_page,name="login"),
    path('logout',views.logout_page,name="logout"),
    path('cart',views.cart_page.as_view(),name="cart"),
    path('remove_cart/<str:cid>',views.remove_cart.as_view(),name="remove_cart"),
    path('fav',views.fav_page,name="fav"),
    path('favviewpage',views.favviewpage.as_view(),name="favviewpage"),
    path('remove_fav/<str:fid>',views.remove_fav.as_view(),name="remove_fav"),
    path('collections/',views.collections.as_view(),name="collections"),
    path('collections/<str:name>',views.collectionsview.as_view(),name="collections"),
    path('collections/<str:cname>/<str:pname>',views.product_details.as_view(),name="product_details"),
    path('addtocart',views.add_to_cart,name="addtocart"),



    





]