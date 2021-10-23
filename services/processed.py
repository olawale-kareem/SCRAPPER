from collections import Counter
from  src.utils import common_words


class WordRefine:

    def __init__(self,soup):
        self.site = soup


    def processed_word(self):

        punctuation = '''©!()-[]{};:'"/\,<>./?@#$%^&*_~…–=0123456789▲©▼'''

        for chars in self.site:
            if chars in punctuation:
                site_body = self.site.replace(chars,'')

        for word in common_words:
            if word in site_body:
                site_body = site_body.replace(word,'')

        refined_site_body = site_body.split()

        for word in refined_site_body:
            if len(word) <= 2:
                refined_site_body.remove(word)

        return refined_site_body

    @staticmethod
    def most_common_words(self,refined_site_body,max_value):

        words_frequency_dict = Counter(refined_site_body)

        words_frequency_dict_max = words_frequency_dict.most_common(max_value)

        keys = []
        values = []

        for i in range(len(words_frequency_dict_max)):
            keys.append(words_frequency_dict_max[i][0].title())
            values.append(int(words_frequency_dict_max[i][1]))

        top_word = keys[0]

        return keys, values, top_word





