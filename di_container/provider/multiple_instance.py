from typing import Any, Callable, Type
from .abstract_provider import AbstractProvider


class MultipleInstanceProvider(AbstractProvider):

    def __init__(self, service_class: Type, creator: Callable):
        super().__init__(service_class, creator)

    def provide(self) -> Any:
        return self._create_instance()
