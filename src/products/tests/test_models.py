from django.test import TestCase
from ..models import Specification, Categorie, Brand, ProductInfo, Product

class SpecificationModelTests(TestCase):
    def test_specification_creation(self):
        spec = Specification.objects.create(name="Color", value="Red")
        self.assertEqual(spec.name, "Color")
        self.assertEqual(spec.value, "Red")


class CategorieModelTests(TestCase):
    def test_category_creation(self):
        category = Categorie.objects.create(name="Computers")
        self.assertEqual(category.name, "Computers")


class BrandModelTests(TestCase):
    def test_brand_creation(self):
        brand = Brand.objects.create(name="AMD")
        self.assertEqual(brand.name, "AMD")


class ProductInfoModelTests(TestCase):
    def setUp(self):
        self.category = Categorie.objects.create(name="Computers")
        self.brand = Brand.objects.create(name="AMD")

    def test_product_info_creation(self):
        product_info = ProductInfo.objects.create(
            sku="123456789",
            name="Test Product",
            description="Test product description",
            price="100.00",
            category=self.category,
            brand=self.brand,
        )
        self.assertEqual(product_info.sku, "123456789")
        self.assertEqual(product_info.name, "Test Product")
        self.assertEqual(product_info.description, "Test product description")
        self.assertEqual(product_info.price, 100.00)
        self.assertEqual(product_info.category, self.category)
        self.assertEqual(product_info.brand, self.brand)


class ProductModelTests(TestCase):
    def setUp(self):
        self.category = Categorie.objects.create(name="Computers")
        self.brand = Brand.objects.create(name="AMD")
        self.product_info = ProductInfo.objects.create(
            sku="123456789",
            name="Test Product",
            description="Test product description",
            price="100.00",
            category=self.category,
            brand=self.brand,
        )

    def test_product_creation(self):
        product = Product.objects.create(type=self.product_info)
        self.assertEqual(product.type, self.product_info)
