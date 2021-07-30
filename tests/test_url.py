import unittest
import requests
from services import url



class TestUrl(unittest.TestCase):

    def test_url(self):
        site = "https://www.google.com"
        action = url.Url(site)
        result = action.url_check(site)
        self.assertIsInstance(result, str)

    def test_url_1(self):
        site = "http://www.google.com"
        action= url.Url(site)
        result = action.url_check(site)
        self.assertEqual(result, site)

    def test_url_2(self):
        site = "www.google.com"
        action= url.Url(site)
        result = action.url_check(site)
        self.assertEqual(result, site)

    def test_url_3(self):
        site = "google.com"
        action= url.Url(site)
        result = action.url_check(site)
        self.assertEqual(result, site)

    def test_url_4(self):
        site = "555.google.com"
        action= url.Url(site)
        result = action.url_check(site)
        self.assertEqual(result, site)

    def test_url_5(self):
        site = "www.airbnb.com"
        action= url.Url(site)
        result = action.url_check(site)
        self.assertEqual(result, site)

    def test_url_processing(self):
        site = "https://www.google.com"
        response = requests.get(site)
        action = url.Url(site)
        result = action.url_processing()
        self.assertEqual(result.status_code, response.status_code)






if __name__ == "__main__":
    unittest.main()



