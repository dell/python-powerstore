from abc import ABC, abstractmethod


class Entity(ABC):

    @abstractmethod
    def get_api_name(self):
        pass

    @abstractmethod
    def execute_api(self):
        pass
