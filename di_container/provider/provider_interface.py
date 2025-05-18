from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any, Type, TYPE_CHECKING

if TYPE_CHECKING:
    from ..container import Container


class ProviderInterface(ABC):

    @abstractmethod
    def provide(self) -> Any:
        pass

    @abstractmethod
    def get_service_class(self) -> Type:
        pass

    @abstractmethod
    def set_container(self, container: Container):
        pass
