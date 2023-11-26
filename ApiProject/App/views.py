from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Inventory
from .serializers import InventorySerializer
# Create your views here.
@api_view()
def Inventory_list(request):
        queryset = Inventory.objects.all()
        serializer1 = InventorySerializer(queryset, many=True)
        return Response(serializer1.data)
@api_view()
def Inventory_detail(request, id):
        inventory = get_object_or_404(Inventory, id=id)
        serializer = InventorySerializer(inventory)
        return Response(serializer.data)