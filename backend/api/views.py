from django.shortcuts import render
from .models import Order

# Create your views here.
from rest_framework import viewsets, serializers


class OrderViewSet(viewsets.ModelViewSet):
    """DRF Version of Order View Set."""

    class OrderSerializer(serializers.ModelSerializer):
        class Meta:
            model = Order
            fields = "__all__"

    serializer_class = OrderSerializer
    queryset = Order.objects.all()