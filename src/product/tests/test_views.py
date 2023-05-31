from django.conf import settings
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from ..models import Brand, Category, SubCategory, Type, BaseInfo
import hashlib
import os
from users.models import TuxTechUser

from django.test import TestCase
from django.urls import reverse


class BrandListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Brand.objects.create(name="Intel", logo_type="png", logo="logos/logo.png")
        Brand.objects.create(name="AMD", logo_type="png", logo="logos/logo.png")
        TuxTechUser.objects.create_user("testuser", "test@test.com", "testpassword")

    # CLIENT !TODO needs auth headers!

    def setUp(self):
        self.client.login(username="testuser", password="testpassword")

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get("/products/api/brands/")
        self.assertEqual(response.status_code, 401)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse("brands-list"))
        self.assertEqual(response.status_code, 401)

    def test_lists_all_brands(self):
        response = self.client.get(reverse("brands-list"))
        self.assertEqual(response.status_code, 401)
        # self.assertTrue(len(response.data) == 2)


class CategoryListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Category.objects.create(
            name="Computers",
            description="Computers category",
            image="logos/logo512.png",
            _sku_prefix="C",
        )

        TuxTechUser.objects.create_user(
            username="testuser", email="test@test.com", password="testpassword"
        )

    # CLIENT needs auth headers!

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get("/products/api/categories/")
        self.assertEqual(response.status_code, 401)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse("categories-list"))
        self.assertEqual(response.status_code, 401)

    def test_lists_all_categories(self):
        response = self.client.get(reverse("categories-list"))
        self.assertEqual(response.status_code, 401)
        self.assertTrue(len(response.data) == 1)
