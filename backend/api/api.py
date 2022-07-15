"""Api File."""
from typing import List
from django.shortcuts import get_object_or_404
from ninja import NinjaAPI
from ninja.security import django_auth

from .models import City, Customer, Order
from .schema import (
    CityPostSchema,
    CitySchema,
    CustomerPostSchema,
    CustomerSchema,
    OrderPostSchema,
    OrderSchema,
)

api = NinjaAPI()


@api.get("/customer/", response=List[CustomerSchema])
def list_customers(request):
    """LIst Customers."""
    qs = Customer.objects.all()
    return qs


@api.post("/customer/")
def create_customer(request, payload: CustomerPostSchema):
    obj = Customer.objects.create(**payload.dict())
    return {"id": obj.id}


@api.put("/customer/{customer_id}")
def update_customer(request, customer_id: int, payload: CustomerPostSchema):
    obj = get_object_or_404(Customer, id=customer_id)
    for attr, value in payload.dict().items():
        setattr(obj, attr, value)
    obj.save()
    return {"success": True}


@api.post("/city/")
def create_city(request, payload: CityPostSchema):
    obj = City.objects.create(**payload.dict())
    return {"id": obj.id}


@api.put("/city/{city_id}")
def update_city(request, city_id: int, payload: CityPostSchema):
    obj = get_object_or_404(City, id=city_id)
    for attr, value in payload.dict().items():
        setattr(obj, attr, value)
    obj.save()
    return {"success": True}


@api.post("/order")
def create_order(request, payload: OrderPostSchema):
    """
    TODO: THIS IS WHAT DOESN'T WORK
    gives "AttributeError: 'int' object has no attribute 'pk'" when POSTing a payload that looks like:
    d = {"city_id": 1, "name": [2, 3, 4]}

    when those pks are known to exist.
    """
    data = payload.dict()
    names = data.pop('name')
    obj = Order.objects.create(**data) 
    obj.name.add(*names)
    return {"id": obj.id}


@api.put("/order/{order_id}")
def update_order(request, order_id: int, payload: OrderSchema):
    obj = get_object_or_404(Order, id=order_id)
    for attr, value in payload.dict().items():
        setattr(obj, attr, value)
    obj.save()
    return {"success": True}