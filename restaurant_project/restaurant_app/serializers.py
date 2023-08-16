from rest_framework import serializers
from .models import DeliveryCrew, MenuItem, Order, Cart

class DeliveryCrewSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryCrew
        fields = '__all__'

class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = '__all__'

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    items = MenuItemSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = '__all__'