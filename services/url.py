import requests
import re



class Url:

    def __init__(self, url):
        self.url = url
    
   
    @property
    def url(self):
        return self._url

    def url_check(self, url):
    
        website_regex_pattern = r'(https?:\/\/)?(www\.)[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,4}\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)|(https?:\/\/)?(www\.)?(?!ww)[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,4}\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)'
        
        website_validation = re.match(website_regex_pattern,url)

        if website_validation == None:
            while website_validation == None:
                valid_url = input(f'Wrong url ({url}) entered.Please input a valid url: ')
                website_validation = re.match(website_regex_pattern,valid_url)
                website_validation = website_validation
            return valid_url
        else:
            return url


    @url.setter
    def url(self, url):
        valid_url = self.url_check(url) 
        self._url = valid_url


    def url_processing(self):

        try:
            response = requests.get(self.url)
        except Exception:
            return False
        else:
            return response 
            



