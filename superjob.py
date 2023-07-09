import requests

from API import Api

from vacancy import Vacancy

class SuperJob(Api):

    key = 'v3.r.137667496.d47121d0f5b4e9f166c5e2cc520fae8b8c5f053b.e3a79ed388429a59d29b4672e7ed05cee8525b5a'

    def get_page(self, text):

        if text is not None:

            params = {"keyword": text}

        else:

            params = {}

        return requests.get("https://api.superjob.ru/2.0/vacancies/", params, headers={'X-Api-App-Id': self.key})

    def to_file(self, reform):

        vacs = [Vacancy(name=vacancy['profession'], url=vacancy['link'], salary={"from": vacancy["payment_from"],"to": vacancy["payment_to"]}) for vacancy in
                reform["objects"]]

        return vacs