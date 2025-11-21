from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any, Type, TYPE_CHECKING
from depydency.inject import Inject

if TYPE_CHECKING:
    from depydency.abc_container import AbcContainer


class AbcProvider(ABC):
    _container: AbcContainer

    @abstractmethod
    def provide(self, inject: Inject) -> Any:
        pass

    @abstractmethod
    def get_dependency_type(self) -> Type:
        pass

    def get_container(self) -> AbcContainer:
        return self._container

    def set_container(self, container: AbcContainer):
        self._container = container
