from ast import Mod

from ninja import ModelSchema

from .models import City, Customer, Order


class CitySchema(ModelSchema):
    """City Schema."""

    class Config:
        """Config."""

        model = City
        model_fields = "__all__"


class CityPostSchema(ModelSchema):
    """City Post Schema"""

    class Config:
        """Config."""

        model = City
        model_exclude = ["id"]


class CustomerSchema(ModelSchema):
    """Customer Schema."""

    class Config:
        """Config."""

        model = Customer
        model_fields = "__all__"


class CustomerPostSchema(ModelSchema):
    """Customer Post Schema"""

    class Config:
        """Config."""

        model = Customer
        model_exclude = ["id"]


class OrderSchema(ModelSchema):
    """Order Schema."""

    class Config:
        """Config."""

        model = Order
        model_fields = "__all__"


class OrderPostSchema(ModelSchema):
    """Order Post Schema"""

    class Config:
        """Config."""

        model = Order
        model_exclude = ["id"]
