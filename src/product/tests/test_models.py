from django.conf import settings
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from ..models import Brand, Category, SubCategory, Type, BaseInfo
import hashlib
import os


class TestProductModels(TestCase):
    def setUp(self):
        test_image_path = os.path.join(
            settings.BASE_DIR, "product/tests/media/logo.png"
        )
        with open(test_image_path, "rb") as img:
            uploaded_image = SimpleUploadedFile(
                name="logo.png",
                content=img.read(),
                content_type="image/png",
            )

            self.brand = Brand.objects.create(
                name="TuxTechEe", logo=uploaded_image, logo_type="png"
            )
        self.category = Category.objects.create(
            name="Computers",
            description="Computers, laptops, and related devices.",
            image="categories/computers.png",
        )
        self.sub_category = SubCategory.objects.create(
            name="Laptops",
            description="Portable computers.",
            category=self.category,
        )
        self.type = Type.objects.create(
            name="Hybrid Laptops",
            description="Laptops with detachable keyboards.",
            type=self.sub_category,
        )
        self.base_info = BaseInfo.objects.create(
            name="Dell XPS 13",
            description="A high-performance ultrabook.",
            category=self.category,
            subCategory=self.sub_category,
            ptype=self.type,
            brand=self.brand,
        )

    def test_image_hashing(self):
        with open(self.brand.logo.path, "rb") as img:
            file_content = img.read()
            expected_hash = hashlib.sha256(file_content).hexdigest()

        self.assertEqual(self.brand.logo_hash, expected_hash)

    def test_category_created(self):
        self.assertEqual(self.category.name, "Computers")
        self.assertEqual(
            self.category.description, "Computers, laptops, and related devices."
        )
        self.assertEqual(self.category.image, "categories/computers.png")

    def test_sub_category_created(self):
        self.assertEqual(self.sub_category.name, "Laptops")
        self.assertEqual(self.sub_category.description, "Portable computers.")
        self.assertEqual(self.sub_category.category, self.category)

    def test_type_created(self):
        self.assertEqual(self.type.name, "Hybrid Laptops")
        self.assertEqual(self.type.description, "Laptops with detachable keyboards.")
        self.assertEqual(self.type.type, self.sub_category)

    def test_base_info_created(self):
        self.assertEqual(self.base_info.name, "Dell XPS 13")
        self.assertEqual(self.base_info.description, "A high-performance ultrabook.")
        self.assertEqual(self.base_info.category, self.category)
        self.assertEqual(self.base_info.subCategory, self.sub_category)
        self.assertEqual(self.base_info.ptype, self.type)
        self.assertEqual(self.base_info.brand, self.brand)
        self.assertEqual(self.base_info.is_new, True)
