from django.core.management.base import BaseCommand
import random
from ...models.brand import Brand
from ...models.info import Info
from ...models.unit import Unit
from ...models.categorie import Categorie
from ...models.specification import Specification


class Command(BaseCommand):
    help = "Create sample data for the products app."

    def handle(self, *args, **options):
        create_sample_data()
        self.stdout.write(self.style.SUCCESS("Sample data created successfully!"))


def create_sample_data():
    brands = ["AMD", "Intel", "NVIDIA", "Samsung", "Apple"]
    categories = ["Computers", "Servers", "Mobile Devices"]

    # Create brands
    for brand_name in brands:
        Brand.objects.get_or_create(name=brand_name)

    # Create categories
    for category_name in categories:
        Categorie.objects.get_or_create(name=category_name)

    # Create sample specifications
    specifications = [
        {"name": "color", "value": "red"},
        {"name": "size", "value": "12 inches"},
        {"name": "resolution", "value": "4k UHD"},
    ]

    # Create sample products
    products = [
        {
            "sku": "P-0001",
            "name": "Product 1",
            "description": "Description for Product 1",
            "price": 100.00,
            "category": Categorie.objects.get(name="Computers"),
            "brand": Brand.objects.get(name="AMD"),
        },
        {
            "sku": "P-0002",
            "name": "Product 2",
            "description": "Description for Product 2",
            "price": 200.00,
            "category": Categorie.objects.get(name="Servers"),
            "brand": Brand.objects.get(name="Intel"),
        },
    ]

    for product_data in products:
        product_info = Info(**product_data)
        product_info.save()

        for spec_data in random.sample(
            specifications, random.randint(1, len(specifications))
        ):
            spec, _ = Specification.objects.get_or_create(**spec_data)
            product_info.specifications.add(spec)

    print("Sample data created successfully!")
