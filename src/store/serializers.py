from dataclasses import fields
from rest_framework import serializers
from .models import Item, OrderItem, Order





class ItemSerializers(serializers.ModelSerializer):
    class Meta:
        model = Item

        fields = "__all__"


class OrderItemSerializers(serializers.ModelSerializer):
    class Meta:
        model = OrderItem

        fields = "__all__"


class OrderSerializers(serializers.ModelSerializer):
    class Meta:
        model = Order

        fields = "__all__"
