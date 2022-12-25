from django.urls import path
from . import views

urlpatterns = [
        path('',views.home,name='home'),
        path('about',views.about.as_view(),name='about'),
        path('register',views.register,name='register'),
        path('login',views.login_page,name='login'),
        path('logout',views.logout_page,name='logout'),
        path('cart',views.cart_page,name='cart'),
        path('favourite',views.fav_page,name='favourite'),
        path('remove_cart/<str:cid>',views.remove_cart,name='remove_cart'),
        path('remove_fav/<str:cid>',views.remove_fav,name='remove_fav'),
        path('collections',views.collections,name='collections'),
        path('collections/<str:name>',views.collectionsview,name='collections'),
        path('collections/<str:cname>/<str:pname>',views.product_details,name='product_details'),
        path('addtocart',views.add_to_cart,name='addtocart'),
        path('favor',views.favor_page,name='favor'),
        path('contact',views.contact,name='contact'),

]