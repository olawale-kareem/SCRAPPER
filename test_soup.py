import unittest
import requests
from services import soup



class TestSoup(unittest.TestCase):

    def test_get_url(self):
        site = "https://www.google.com"
        response = requests.get(site)
        action= soup.Soup(response)
        result = action.get_url()
        self.assertIsInstance(result, str)



    def test_get_url_1(self):
        site = "https://www.facebook.com"
        response = requests.get(site)
        action= soup.Soup(response)
        result = action.get_url()
        self.assertNotEqual(result, 10)



    def test_get_url_2(self):
        site = "https://www.netflix.com"
        response = requests.get(site)
        action= soup.Soup(response)
        result = action.get_url()
        self.assertNotEqual(result, '')


    def test_get_url_3(self):
        site = "https://www.airbnb.com"
        response = requests.get(site)
        action= soup.Soup(response)
        result = action.get_url()
        self.assertNotEqual(result, False)


    def test_get_url_4(self):
        site = "https://www.airbnb.com"
        response = requests.get(site)
        action= soup.Soup(response)
        result = action.get_url()
        self.assertNotEqual(result, False)

    def test_get_url_5(self):
        site = "https://www.google.com"
        response = requests.get(site)
        action= soup.Soup(response)
        result = action.get_url()
        self.assertIsNotNone(result)



if __name__ == "__main__":
    unittest.main()



