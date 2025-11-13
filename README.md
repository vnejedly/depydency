# di_tree — Dependency Injection (DI) helper library

A small, lightweight dependency-injection/locator helper used in this project to register and resolve services by type or by name. This README is a stub demonstrating package purpose, quick usage and multiple Markdown features (headings, lists, tables, code blocks, images, captions, inline code, blockquotes, and task lists).

---

## Quick summary

di_tree provides:
- a container/locator abstraction for registering providers
- several provider types: alias, explicit value, explicit callable, auto-resolve
- lookup by Python type (class) or named keys

It is intentionally minimal and easy to embed in small projects.

---

## Table of contents

1. Installation
2. Concepts
3. Basic usage
4. Providers
5. Advanced examples
6. Reference & testing
7. Notes, links and credits

---

## Installation

Clone the repository (example):

```bash
git clone <repo-url>
cd di-test
# Use project sources directly (no pip package in this stub)
```

You can run the example in `src/`:

```bash
python -m src.__main__
```

---

## Concepts

- Container: holds providers and resolves instances.
- Provider: an object that knows how to produce a value for a type/name.
- Alias: map an interface/abstract type to a concrete implementation.
- ExplicitValue: always return the given instance/value.
- ExplicitCallable: call a factory function to produce the instance.
- AutoResolve: (when available) try to construct a type automatically.

> Tip: use `python -u` (unbuffered) when running long-running processes in containers to see output immediately.

---

## Basic usage

Example: register providers and get services


File: a_package/abc_speaker_interface.py

```python
from abc import ABC, abstractmethod


class AbcSpeakerInterface(ABC):

    instances_count: int = 0

    def __init__(self):
        AbcSpeakerInterface.instances_count += 1
        self.instance_num: int = self.instances_count
    
    @abstractmethod
    def speak(self) -> str:
        pass
```


File: a_package/speaker_a.py

```python
from a_package.abc_speaker_interface import AbcSpeakerInterface


class SpeakerA(AbcSpeakerInterface):
    def speak(self) -> str:
        return f"I am instance {self.instance_num} of speaker A"
```


File: a_package/a_class.py

```python
from a_package.speaker_a import SpeakerA
from a_package.abc_speaker_interface import AbcSpeakerInterface
from di_tree.inject import TypeInject, NameInject


class AClass:

    speaker_1: AbcSpeakerInterface = TypeInject()
    speaker_2: AbcSpeakerInterface = TypeInject()
    script_name: str = NameInject()

    def name(self) -> str:
        return (
            f"Script name: {self.script_name}\n"
            f"Class A (instances count = {SpeakerA.instances_count})\n"
            f"Speaker 1: {self.speaker_1.speak()}\n"
            f"Speaker 2: {self.speaker_2.speak()}\n"
        )
```


File: container.py

```python
from a_package.abc_speaker_interface import AbcSpeakerInterface
from a_package.speaker_a import SpeakerA
from di_tree.abc_container import AbcContainer
from di_tree.provider.alias import Alias
from di_tree.provider.explicit_value import ExplicitValue
from di_tree.provider.explicit_callable import ExplicitCallable


class Container(AbcContainer):
    def setup(self):
        def create_speaker_a() -> SpeakerA:
            return SpeakerA()

        """Setup dependencies here"""
        self.set_provider(Alias(AbcSpeakerInterface, SpeakerA))
        self.set_provider(ExplicitCallable(SpeakerA, create_speaker_a))
        # self.set_provider(ExplicitValue(SpeakerA()))
        self.set_named_provider("script_name", ExplicitValue("Kravina 0.9"))
```


File: __main__.py

```python
from a_package.a_class import AClass
from container import Container


container = Container()
a_class_1 = container.get_by_type(AClass)
a_class_2 = container.get_by_type(AClass)

print(a_class_1.name())
print(a_class_2.name())

```