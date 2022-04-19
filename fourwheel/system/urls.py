from django.urls import path,include
from django.contrib import admin
from system import views

urlpatterns = [
    path('', views.home, name = "home"),

    path('carlist/', views.car_list, name = "car_list"),
    path('createOrder/', views.order, name = "order_create"),

    path('(?P<id>\d+)/edit/', views.car_update, name = "car_edit"),


    path('(?P<id>\d+)/', views.car_detail, name = "car_detail"),
    path('detail/(?P<id>\d+)/', views.order_detail, name = "order_detail"),

    path('(?P<id>\d+)/delete/', views.car_delete, name = "car_delete"),
    path('(?P<id>\d+)/deleteOrder/', views.order_delete, name = "order_delete"),

    path('contact/', views.contact, name = "contact"),

    path('newcar/', views.newcar, name = "newcar"),
    path('(?P<id>\d+)/like/', views.like_update, name = "like"),
    path('popularcar/', views.popular_car, name = "popularcar"),
    
    #--------------Settings url-------------#
    
    path('admincar/', views.admin_index, name='adminIndex'),
    path('listOrder/', views.order_list, name = "order_list"),
    path('(?P<id>\d+)/editOrder/', views.order_update, name = "order_edit"),
    path('(?P<id>\d+)/deleteOrder/', views.order_delete, name = "order_delete"),
    path('create/', views.addcar, name = "car_create"),
    path('message/', views.admin_msg, name='message'),
    path('(?P<id>\d+)/deletemsg/', views.msg_delete, name = "msg_delete"),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
]
