from hh import Hh

from superjob import SuperJob

from vacancy import Vacancy

from write_vacs import WriteVacs

from pprint import pprint

import json

def print_vac(vac:Vacancy):

    print(f'Должность: {vac["name"]}')
    print(f'Зарплата: {vac["salary"]}')
    print(f'Ссылка: {vac["url"]}')


def print_sorted(keyword, salary):
    with open("vacancy.json", 'r') as file:
        data = json.load(file)
        for vac in data:
            if keyword is None and salary <= vac["salary"]:
                print_vac(vac)
                print()
            elif keyword is not None and keyword in vac["name"]:
                print_vac(vac)
                print()



def main():

    print('Введи вакансию')
    keyword = input()

    a = Hh()
    b = SuperJob()

    hh_page = a.get_page(keyword).json()
    superjob_page = b.get_page(keyword).json()

    hh_page = a.to_file(hh_page)
    superjob_page = b.to_file(superjob_page)

    output = []

    output.extend(hh_page)
    output.extend(superjob_page)

    print(f'Найденно вакансий: {len(output)}')
    if len(output) == 0:

        exit()

    print(f'Сколько вакансий вывести?')

    while True:

        try:

            number = int(input())

        except ValueError:

            print("Пожалуйста, введи число")
            continue

        if len(output) > 0 and 0 < number <= len(output):

            break

        else:

            print(f"Пожалуйста, введи число от 1 до {len(output)}")

    c = WriteVacs()


    c.write('vacancy.json', output)
    top = c.top_vacs('vacancy.json', number)

    print("Вот лучшие из вакансий, что я нашел:")

    for vac in top:
        print_vac(vac)
        print()

    while True:
        print("""Можете выбвести вакансии по ключевым словам или минимальной зарплате.
    Нажмите 1 для ввода ключевого слова
    Нажмите 2 для ввода минимальной зарплаты
    Нажмите 0 для завершения программы""")
        answer = input().strip()

        if answer in ["1", "2"]:
            break
        elif answer == "0":
            exit()
        else:
            print("Пожалуйста, введите число от 1 до 2")

    if answer == "1":
        keyword = input("Введите ключевое слово: ")
        print_sorted(keyword=keyword, salary=None)
    else:
        while True:
            try:
                salary = int(input("Введите минимальную зарплату: "))
                break
            except ValueError:
                print("Пожалуйста, введите число")
                continue

        print_sorted(keyword=None, salary=salary)

    print("Всего доброго!")


if __name__ == '__main__':

    main()
