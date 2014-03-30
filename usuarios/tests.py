import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "manejalo.settings")

from django.test import TestCase

class SimpleTest(TestCase):
    
    def test_basic_addition(self):
        self.assertEqual(1 + 1, 2)

    def test_success(self):
        self.assertTrue(True)