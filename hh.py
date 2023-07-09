from vacancy import Vacancy

from pprint import pprint

import requests

from API import Api

class Hh(Api):

    def get_page(self, text=None):

        if text is not None:

            text = "+".join(text.split(" "))
            params = {"text": f"NAME:{text}"}

        else:

            params = {}

        return requests.get("https://api.hh.ru/vacancies", params)


    def to_file(self, reform):

        vacs = [Vacancy(name=vacancy['name'], url=vacancy['alternate_url'], salary=vacancy['salary']) for vacancy in reform["items"]]

        return vacs




