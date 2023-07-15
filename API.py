from abc import ABC, abstractmethod

class Api(ABC):

    @abstractmethod
    def get_page(self):

        pass

    @abstractmethod
    def to_file(self, reform):

        pass
