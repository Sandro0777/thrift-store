from django.urls import path

from . import views

urlpatterns = [
    path('', views.index,name='index'),
    path('registration',views.user_register,name='registration'),
    path('login', views.admin_login,name='login'),
    #path('login', views.admin_login,name='login'),
    path('adminhome', views.adminhome, name='adminhome'),
    path('user_home', views.user_home, name='user_home'),
    path('add_product',views.add_product, name='add_product'),
    path('admin_view_product', views.admin_view_pro, name="admin_view_product"),
    path('user_details_update', views.user_details_update, name="user_details_update"),
    path('product_update',views.product_update,name="product_update"),
    path('delete_num', views.delete_num, name="delete_num"),
    path('user_product_view', views.user_product_view, name='user_product_view'),




]
