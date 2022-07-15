from django.test import TestCase
from .models import City, Customer, Order

# Create your tests here.
class TestNinjaApi(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.c = City.objects.create(city="this")
        cls.cust_1 = Customer.objects.create(name="Fred")
        cls.cust_2 = Customer.objects.create(name="Junior")
        cls.cust_3 = Customer.objects.create(name="Third")
        cls.payload = {
            "city_id": cls.c.id,
            "name": [cls.cust_1.id, cls.cust_2.id, cls.cust_3.id],
        }

    def test_m2m_ninja(self):
        # TODO: THIS WILL RAISE EXCEPTION
        try:
            response = self.client.post(
                "/api/order", data=self.payload, content_type="application/json"
            )
            self.assertEqual(response.status_code, 200)
        except AttributeError:
            self.fail("ninja m2m failed")

    def test_m2m_drf(self):
        response = self.client.post("/drf-api/orders", data=self.payload, content_type="application/json", follow=True)
        self.assertEqual(response.status_code, 200)