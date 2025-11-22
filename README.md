# Depydency — Dependency Injection (DI) container and Inversion Of Control (IoC) helper library

A lightweight IoC (inversion of control) and DI (dependency-injection) container to register and resolve services by type or by name. I allows the recursive autowiring of the whole dependency tree as well as custom configuration of particular dependencies.

---

## Table of contents

1. Installation
2. Concepts
3. Basic usage
4. Providers
5. Advanced examples

---

## Installation

```bash
pip install depydency
```

---

## Concepts

- Container: holds various dependency providers.
- Provider: an object that knows how to produce the value/instance for a particular dependency ba type or name.
- Alias: map an interface/abstract type to a concrete implementation.
- ExplicitValue: always return the given instance/value.
- ExplicitCallable: call a factory function to produce the instance.
- AutoResolve: FOR INTERNAL USAGE ONLY - (when available) try to construct a type automatically.
---

## Basic usage

Example: register providers and get services


File: a_package/abc_speaker_interface.py

```python
from abc import ABC, abstractmethod


class AbcSpeakerInterface(ABC):
    
    @abstractmethod
    def speak(self) -> str:
        pass

```


File: a_package/speaker_a.py

```python
from a_package.abc_speaker_interface import AbcSpeakerInterface
from a_package.x_class import XClass
from depydency.inject import TypeInject
from typing import Annotated


class SpeakerA(AbcSpeakerInterface):
    instances_count: int = 0

    x_object: Annotated[XClass, TypeInject()]

    def __init__(self):
        SpeakerA.instances_count += 1
        self.instance_num: int = self.instances_count

    def speak(self) -> str:
        return (
            f"I am instance {self.instance_num} of speaker A "
            f"having also an instance of {self.x_object.get_name()}"
        )
```


File: a_package/a_class.py

```python
from a_package.speaker_a import SpeakerA
from a_package.speaker_b import SpeakerB
from a_package.abc_speaker_interface import AbcSpeakerInterface
from depydency.inject import TypeInject, NameInject
from typing import Annotated


class AClass:
    speaker_1: Annotated[AbcSpeakerInterface, TypeInject()]
    speaker_2: Annotated[AbcSpeakerInterface, TypeInject()]
    speaker_3: Annotated[SpeakerB, TypeInject()]
    script_name: Annotated[str, NameInject(default_value="Hovadina")]

    test: str = 'tezt'

    @property
    def info(self) -> str:
        return (
            f"Script name: {self.script_name}\n"
            f"Class A (instances count = {SpeakerA.instances_count})\n"
            f"Speaker 1: {self.speaker_1.speak()}\n"
            f"Speaker 2: {self.speaker_2.speak()}\n"
            f"Speaker 3: {self.speaker_3.speak()}\n"
        )
```


File: container.py

```python
from a_package.abc_speaker_interface import AbcSpeakerInterface
from a_package.speaker_a import SpeakerA
from a_package.speaker_b import SpeakerB
from depydency.abc_container import AbcContainer
from depydency.provider.alias import Alias
from depydency.provider.value import Value
from depydency.provider.callback import Callback
from depydency.provider.abc_creator import AbcCreator
from depydency.inject import Inject


class Container(AbcContainer):
    def setup(self):
        self.provide_type(Alias(AbcSpeakerInterface, SpeakerA))
        self.provide_type(Callback(SpeakerA, self.create_speaker_a))
        self.provide_type(Value(SpeakerB()))
        self.provide_name("script_name", Value("Kravina 0.9"))

    @staticmethod
    def create_speaker_a(provider: AbcCreator, inject: Inject) -> SpeakerA:
        instance = SpeakerA()
        provider.inject_dependencies(instance)
        return instance
```


File: __main__.py

```python
from a_package.a_class import AClass
from container import Container


container = Container()
a_class_1 = container.get_by_type(AClass)
a_class_2 = container.get_by_type(AClass)

print(a_class_1.info)
print(a_class_2.info)        

```