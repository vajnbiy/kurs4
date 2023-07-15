class Vacancy:

    def __init__(self, name, url, salary):

        self.name = name
        self.url = url

        try:

            from_ = salary["from"]

        except TypeError:

            from_ = 0

        try:

            to = salary["to"]

        except TypeError:

            to = 0

        try:

            self.salary = from_ + to

        except TypeError:

            if from_ is None:

                self.salary = to

            else:
                self.salary = from_

    def __eq__(self, other):
        return self.salary == other.salary

    def __gt__(self, other):
        return self.salary > other.salary

    def __lt__(self, other):
        return self.salary < other.salary

    def __ge__(self, other):
        return self.salary >= other.salary

    def __le__(self, other):
        return self.salary <= other.salary

