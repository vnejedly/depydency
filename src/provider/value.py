from typing import Any, Type, TYPE_CHECKING
from di_tree.provider.abc_provider import AbcProvider
from di_tree.inject import Inject


class Value(AbcProvider):
    def __init__(self, value: Any):
        self._value = value

    def provide(self, inject: Inject) -> Any:
        assert inject.unique_instance == False, "Can only inject the actual value"
        return self._value

    def get_dependency_type(self) -> Type:
        return type(self._value)
