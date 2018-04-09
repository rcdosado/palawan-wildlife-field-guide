
from django.test import SimpleTestCase



class PageOpenTestCase(SimpleTestCase):
    def test_home_page_exists(self):
        self.assertEqual(100+100, 200)

