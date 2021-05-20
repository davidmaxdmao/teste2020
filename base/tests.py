from django.test import TestCase

# Create your tests here.
class TesteCi(TestCase):

    def test_sucesso(self):
        self.assertEqual(2, 1)
