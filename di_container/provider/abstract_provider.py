from __future__ import annotations
from ..exceptions.bad_class import BadClassException
from ..exceptions.not_callable import NotCallableException
from .provider_interface import ProviderInterface
from typing import Any, Type, Callable, TYPE_CHECKING
from abc import ABC

if TYPE_CHECKING:
    from ..container import Container


class AbstractProvider(ProviderInterface, ABC):

    _container: Container
    _service_class: Type
    _creator: Callable

    def __init__(self, service_class: Type, creator: Callable):
        if not callable(creator):
            raise NotCallableException(service_class)

        self._service_class = service_class
        self._creator = creator

    def get_service_class(self) -> Type:
        return self._service_class

    def set_container(self, container: Container):
        self._container = container

    def _create_instance(self) -> Any:
        instance = self._creator()
        class_provided = type(instance)
        if class_provided != self._service_class:
            raise BadClassException(self._service_class, class_provided)

        return instance
