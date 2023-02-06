from django.test import TestCase
from restaurant.models import Menu

# Create your tests here.

class MenuItemTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title="Pasta", price=10, inventory=15)
        itemstr = item.__str__()
        
        self.assertEqual(itemstr, "Pasta")