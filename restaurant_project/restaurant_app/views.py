from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import DeliveryCrew, MenuItem, Cart, Order
from .serializers import DeliveryCrewSerializer, MenuItemSerializer, CartSerializer, OrderSerializer

class HomeView(APIView):
    def get(self, request):
        data = {
            "message": "Welcome to the Restaurant API!",
        }
        return Response(data)

class DeliveryCrewList(APIView):
    def get(self, request):
        delivery_crews = DeliveryCrew.objects.all()
        serializer = DeliveryCrewSerializer(delivery_crews, many=True)
        return Response(serializer.data)

class MenuItemList(APIView):
    def get(self, request):
        menu_items = MenuItem.objects.all()
        serializer = MenuItemSerializer(menu_items, many=True)
        return Response(serializer.data)

class CartList(APIView):
    def get(self, request):
        carts = Cart.objects.all()
        serializer = CartSerializer(carts, many=True)
        return Response(serializer.data)

class OrderList(APIView):
    def get(self, request):
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)
