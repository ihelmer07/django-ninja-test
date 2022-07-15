"""Load Data."""
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Base command."""

    help = "Load Data"

    def handle(self, *args, **kargs):
        """Handle command."""
        import faker
        from django.contrib.auth.models import User

        from backend.api.models import City, Customer, Order

        fake = faker.Faker()
        try:
            User.objects.get(username="admin")
        except User.DoesNotExist:
            User.objects.create_superuser(
                username="admin",
                email="test@test.com",
                password="admin1234",
                is_superuser=True,
                is_staff=True,
                first_name="System",
                last_name="Admin",
            )
        print("Created User")

        customers = [Customer(name=fake.first_name()) for _ in range(10)]
        cities = [City(city=fake.city()) for _ in range(10)]

        Customer.objects.bulk_create(customers)
        print("created 10 customers")
        City.objects.bulk_create(cities)
        print("created 10 cities")
