from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
class Customer(models.Model):
    """Model with simple info."""

    name = models.CharField(_("Name"), max_length=50)

    def __str__(self):
        """Str Method override."""
        return self.name


class City(models.Model):
    """Model with simple info."""

    city = models.CharField(_("City"), max_length=3)

    def __str__(self):
        """Str Method override."""
        return self.city


class Order(models.Model):
    """Model with multiple many to many and fk relations."""

    city = models.ForeignKey(City, verbose_name=_("Name"), on_delete=models.CASCADE)
    name = models.ManyToManyField(Customer, verbose_name=_("Customers"))

    def __str__(self):
        """Str Method override."""
        return f"Order {self.pk} for {self.city.name}"
