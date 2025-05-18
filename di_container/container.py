from typing import Any, Dict, Type
from .locator_interface import LocatorInterface
from .provider.provider_interface import ProviderInterface
from .provider.auto_resolve import AutoResolveProvider
from .inject import Inject
 

class Container(LocatorInterface):

    _providers: Dict[str, ProviderInterface]

    def __init__(self):
        self._providers = {}

    def add_provider(self, provider: ProviderInterface):
        service_name = self._get_service_name(provider.get_service_class())
        self._providers[service_name] = provider
        provider.set_container(self)

    def get_service(self, service_class: Type) -> Any:
        service_name = self._get_service_name(service_class)
        if service_name not in self._providers.keys():
            self.add_provider(AutoResolveProvider(service_class))

        return self._providers.get(service_name).provide()

    def inject_dependencies(self, instance: Any, dependencies: Dict[str, Any] = None):
        if dependencies is None:
            dependencies = {}

        for (dep_name, dep_class) in instance.__class__.__annotations__.items():
            if getattr(instance.__class__, dep_name) == Inject:
                setattr(instance, dep_name, dependencies.get(
                    dep_name, self.get_service(dep_class)
                ))

    @staticmethod
    def _get_service_name(service_class: Type) -> str:
        return f"{service_class.__module__}.{service_class.__name__}"
