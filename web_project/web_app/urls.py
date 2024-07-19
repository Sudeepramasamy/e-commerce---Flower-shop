from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home,name="home"),
    path('home/', views.home,name="home"),
    path('signin/',views.register, name='register'),
    path('collections/',views.collections, name='collections'),
    path('collections/<str:name>',views.collectionsview, name='collections'),
    path('collections/<str:cname>/<str:pname>',views.product_details, name='product_details'),
    path('addtocart',views.add_to_cart, name='addtocart'),
    path('cart/',views.cart_view, name='cart'),
    path('order/',views.order, name='order'),
     path('logout/',views.logout_page, name='logout'),
    path('remove_cart/<str:cid>',views.remove_cart, name='remove_cart'),
    path('login/',auth_views.LoginView.as_view(template_name='login.html'),name='login'), 
    path('logout/',auth_views.LoginView.as_view(template_name='logout.html'),name='logout'),
  
]