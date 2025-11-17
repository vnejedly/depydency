from __future__ import annotations
from typing import Any, Type, TYPE_CHECKING
from di_tree.provider.abc_provider_interface import AbcProviderInterface
from di_tree.inject import Inject

if TYPE_CHECKING:
    from di_tree.abc_container import AbcContainer


class Alias(AbcProviderInterface):

    _container: AbcContainer
    _alias_type: Type
    _target_type: Type

    def __init__(self, alias_type: Type, target_type: Type):
        self._alias_type = alias_type
        self._target_type = target_type

    def provide(self, inject: Inject) -> Any:
        inject.set_dependency_id(dependency_type=self._target_type)
        return self._container.get_dependency(inject)

    def get_dependency_type(self) -> Type:
        return self._alias_type

    def set_container(self, container: AbcContainer):
        self._container = container
