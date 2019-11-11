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

    def test_delete_location(self):
        self.location2 = Location(name="Nairobi")
        Location.objects.filter(name="Nairobi").delete()
        location_2 = Location.objects.filter(name="Nairobi")
        self.assertEqual(len(location_2),0) 

    def test_update_location(self): 
        self.location.name = "Nakuru"
        self.location.save()
        location = Location.objects.filter(name="Nakuru").first()
        self.assertEqual(location.name,"Nakuru") 


class CategoryTestClass(TestCase):
    def setUp(self):
        self.category = Category(title="fashion")

    def tearDown(self):
        Category.objects.filter(title="fashion").delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.category,Category))

    def test_delete_category(self):
        self.category2 = Category(title="genetics")
        Category.objects.filter(title="genetics").delete()
        category2 = Category.objects.filter(title="genetics")
        self.assertEqual(len(category2),0) 

