from abc import ABC, abstractmethod
from typing import Type, Any


class LocatorInterface(ABC):

    @abstractmethod
    def get_service(self, service_class: Type) -> Any:
        pass
