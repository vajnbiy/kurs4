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