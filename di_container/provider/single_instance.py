from typing import Any, Callable, Type
from .abstract_provider import AbstractProvider


class SingleInstanceProvider(AbstractProvider):

    _instance: Any

    def __init__(self, service_class: Type, creator: Callable):
        super().__init__(service_class, creator)
        self._instance = None

    def provide(self) -> Any:
        if self._instance is None:
            self._instance = self._create_instance()

        return self._instance
