from django.urls import path
from . import views

urlpatterns = [
    path('detail/<int:id>/', views.Inventory_detail, name="detail"),
    path('Inventory/',views.Inventory_list, name="Inventory_detail")
]
