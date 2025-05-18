from __future__ import annotations
from typing import Any, Type, TYPE_CHECKING
from .provider_interface import ProviderInterface

if TYPE_CHECKING:
    from ..container import Container


class Alias(ProviderInterface):

    _container: Container
    _alias_class: Type
    _target_class: Type

    def __init__(self, alias_class: Type, target_class: Type):
        self._alias_class = alias_class
        self._target_class = target_class

    def provide(self) -> Any:
        return self._container.get_service(self._target_class)

    def get_service_class(self) -> Type:
        return self._alias_class

    def set_container(self, container: Container):
        self._container = container
