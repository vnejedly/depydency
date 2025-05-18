from typing import Type, Any
from ..provider.single_instance import SingleInstanceProvider
import importlib


class AutoResolveProvider(SingleInstanceProvider):

    def __init__(self, service_class: Type):
        super().__init__(service_class, getattr(self, '_creator'))

    def _creator(self) -> Any:
        module = importlib.import_module(self._service_class.__module__)
        class_reference = getattr(module, self._service_class.__name__)

        instance = class_reference()
        self._container.inject_dependencies(instance)

        return instance
