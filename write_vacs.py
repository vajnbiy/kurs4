from abc import ABC

import json

from vacancy import Vacancy


class WriteVacs:

    @staticmethod
    def write(path, list_):

        output = []

        for i in list_:

            output.append(i.__dict__)

        open(path, "w").close()

        with open(path, 'w') as file:


            file.write(str(json.dumps(output, indent=2, ensure_ascii=False)))

    @staticmethod
    def top_vacs(path, number):

        with open(path, 'r') as file:

            data = json.load(file)
            data = sorted(data, key=lambda d: d['salary'], reverse=True)

            try:

                output = data[0:number]

            except IndexError:

                output = data

        return output

