from django.test import TestCase
from .models import Location, Image, Category
# Create your tests here.

class LocationTestClass(TestCase):
    def setUp(self):
        self.location = Location(name="Ngong Rd, Kenya")

    def tearDown(self):
        Location.objects.filter(name="Ngong Rd, Kenya").delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.location,Location))

class CategoryTestClass(TestCase):
    def setUp(self):
        self.category = Category(title="fashion")

    def tearDown(self):
        Category.objects.filter(title="fashion").delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.category,Category))

