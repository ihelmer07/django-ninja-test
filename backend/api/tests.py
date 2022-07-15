from django.test import TestCase
from .models import City, Customer, Order

# Create your tests here.
class TestNinjaApi(TestCase):
    def test_m2m(self):
        c = City.objects.create(city="this")
        cust_1 = Customer.objects.create(name="Fred")
        cust_2 = Customer.objects.create(name="Junior")
        cust_3 = Customer.objects.create(name="Third")
        payload = {"city_id": c.id, "name": [cust_1.id, cust_2.id, cust_3.id]}
        self.assertRaises(response = self.client.post('/api/order', data=payload, content_type='application/json'))

