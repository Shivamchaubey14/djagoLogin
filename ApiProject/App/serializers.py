from decimal import Decimal
from rest_framework import serializers
from .models import Inventory
class InventorySerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=255)
    price = serializers.DecimalField(max_digits=5, decimal_places=2)
    unit = serializers.IntegerField()
    price_after_gst = serializers.SerializerMethodField(method_name='calculate_tax')

    def calculate_tax(self, inventory: Inventory) -> float:
        return inventory.unit * Decimal(1.1) * inventory.price