"""
URL configuration for restaurant_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from restaurant_app.views import HomeView, DeliveryCrewList, MenuItemList, CartList, OrderList

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('delivery-crews/', DeliveryCrewList.as_view(), name='delivery-crew-list'),
    path('menu-items/', MenuItemList.as_view(), name='menu-item-list'),
    path('carts/', CartList.as_view(), name='cart-list'),
    path('orders/', OrderList.as_view(), name='order-list'),
]