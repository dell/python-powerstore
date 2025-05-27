"""Base class for Entity."""

from abc import ABC, abstractmethod

class Entity(ABC):
    """
    Base class for Entity.

    This class provides the basic structure for entities in the system.
    It defines the interface for getting the API name and executing an API call.
    """

    @abstractmethod
    def get_api_name(self):
        """
        Returns the API name for the entity.

        This method must be implemented by any subclass of Entity.
        It should return the name of the API that corresponds to the entity.
        """

    @abstractmethod
    def execute_api(self, api_name):
        """
        Executes an API call for the entity.

        This method must be implemented by any subclass of Entity.
        It should take the API name as input and execute the corresponding API call.

        Args:
            api_name (str): The name of the API to execute.
        """
