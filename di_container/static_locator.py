from typing import Type, Any
from .locator_interface import LocatorInterface


class StaticLocator:

    locator: LocatorInterface

    @classmethod
    def get(cls, service_class: Type) -> Any:
        return cls.locator.get_service(service_class)
