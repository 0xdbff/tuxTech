from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from django.conf import settings
from product.models import (
    Brand,
    Category,
    SubCategory,
    Type,
    BaseInfo,
    Variant,
    Specification,
)
from users.models import Client
from .models import Info, Item
import os


class InfoModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = Client.objects.create(username="testuser", password="testpassword")
        cls.info = Info.objects.create(user=cls.user)

    def test_info_creation(self):
        self.assertIsInstance(self.info, Info)

    def test_info_save_method(self):
        self.assertEqual(self.user.cart, self.info)

    def test_info_string_representation(self):
        self.assertEqual(str(self.info), f"Cart of user {self.user.username}")


class ItemModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        cls.user = Client.objects.create(username="testuser", password="testpassword")
        cls.info = Info.objects.create(user=cls.user)

        test_image_path = os.path.join(
            settings.BASE_DIR, "product/tests/media/logo.png"
        )
        with open(test_image_path, "rb") as img:
            uploaded_image = SimpleUploadedFile(
                name="logo.png",
                content=img.read(),
                content_type="image/png",
            )

            cls.brand = Brand.objects.create(
                name="TuxTechEe", logo=uploaded_image, logo_type="png"
            )

        cls.category = Category.objects.create(
            name="Computers",
            description="Computers, laptops, and related devices.",
            image="categories/computers.png",
        )

        cls.sub_category = SubCategory.objects.create(
            name="Laptops",
            description="Portable computers.",
            category=cls.category,
        )

        cls.type = Type.objects.create(
            name="Hybrid Laptops",
            description="Laptops with detachable keyboards.",
            type=cls.sub_category,
        )

        cls.base_info = BaseInfo.objects.create(
            name="Dell XPS 13",
            description="A high-performance ultrabook.",
            category=cls.category,
            subCategory=cls.sub_category,
            ptype=cls.type,
            brand=cls.brand,
        )

        spec1 = Specification.objects.create(
            key="color",
            value="Red",
        )

        spec2 = Specification.objects.create(
            key="size",
            value="Large",
        )

        cls.variant = Variant.objects.create(
            name="Variant1",
            ean="1234567890123",
            is_default=True,
            mediafiles_hash="default_hash",
            price="999.99",
            info=cls.base_info,
        )
        cls.variant.specifications.add(spec1, spec2)

        cls.item = Item.objects.create(cart=cls.info, variant=cls.variant)

    def test_item_creation(self):
        self.assertIsInstance(self.item, Item)

    def test_item_string_representation(self):
        expected_string = f"{self.variant.name} ({self.variant.sku}) x {self.item.quantity} in cart {self.info.user.id}"
        self.assertEqual(str(self.item), expected_string)

    def test_unique_together_constraint(self):
        with self.assertRaises(Exception):
            Item.objects.create(cart=self.info, variant=self.variant)
