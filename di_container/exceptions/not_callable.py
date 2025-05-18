from typing import Type


class NotCallableException(Exception):

    def __init__(self, service_class: Type):
        self.service_class = service_class
        super().__init__(
            f"Creator function for service {service_class.__module__}.{service_class.__name__} is not callable"
        )
