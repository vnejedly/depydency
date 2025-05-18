from typing import Type


class BadClassException(Exception):

    def __init__(self, class_expected: Type, class_provided: Type):
        self.class_expected = class_expected
        self.class_provided = class_provided

        name_expected = class_expected.__module__ + class_expected.__name__
        name_provided = class_provided.__module__ + class_provided.__name__

        super().__init__(
            f"Expected class {name_expected}, got {name_provided} from provider"
        )
