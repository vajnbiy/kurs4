from hh import Hh

from superjob import SuperJob

from vacancy import Vacancy

from write_vacs import WriteVacs

from pprint import pprint

def print_vac(vac:Vacancy):

    print(f'Должность: {vac["name"]}')
    print(f'Зарплата: {vac["salary"]}')
    print(f'Ссылка: {vac["url"]}')


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


    c.write('vacancy.txt', output)
    top = c.top_vacs('vacancy.txt', number)

    print("Вот лучшие из вакансий, что я нашел:")

    for vac in top:
        print_vac(vac)
        print()

    print("Всего доброго!")


if __name__ == '__main__':

    main()

