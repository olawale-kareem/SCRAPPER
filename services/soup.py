from bs4 import BeautifulSoup
from requests.models import Response


class Soup:
    
    def __init__(self,response):
        self.response = response

    def get_url(self):  
        soup = BeautifulSoup(self.response.content, 'html.parser')
        site_body = soup.body.text.strip()
        return site_body


