from typing import Type, Any
from depydency.provider.abc_creator import AbcCreator
from depydency.inject import Inject
import importlib


class AutoResolve(AbcCreator):
    def __init__(self, dependency_type: Type):
        self._dependency_type = dependency_type
        self._instance = None

    def _creator(self, inject: Inject) -> Any:
        module = importlib.import_module(self.get_dependency_type().__module__)
        type_reference = getattr(module, self.get_dependency_type().__name__)
        
        instance = type_reference()
        self.inject_dependencies(instance)
        
        return instance
