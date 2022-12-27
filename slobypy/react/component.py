# pylint: disable=unnecessary-pass

from __future__ import annotations

# Built-in
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, Generator, Type

from slobypy import SlApp
from slobypy.react.scss import SCSS

if TYPE_CHECKING:
    from slobypy.react import BaseElement

__all__ = (
    "Component",
    "SloContext")


class SloContext:

    def __init__(self, name):
        self.name = name

    def __setattr__(self, key, value):
        super().__setattr__(key, value)

    def __getattribute__(self, item):
        return super().__getattribute__(item)



class Component(ABC):

    def __new__(cls, props=None, *args, **kwargs):
        # noinspection PyTypeChecker
        component = super().__new__(cls, *args, **kwargs)
        # noinspection PyProtectedMember
        for registered_component in SlApp._components:
            if registered_component["component"] == cls:
                component.meta_data = registered_component["metadata"]

        component.props = {} if props is None else props
        component.style = SCSS()

        return component

    @property
    @abstractmethod
    def name(self) -> str:
        """
        Name of the component.
        """
        pass

    @abstractmethod
    def body(self) -> Generator[Type[BaseElement], None, None]:
        """
        Use the elements here with yield syntax.
        """
        pass

    def render(self):
        """
        Get the component body with html elements and tags.
        """
        return ''.join([element.render() for element in self.body()])

    # noinspection PyMethodMayBeStatic
    def render_js(self):
        """
        Get any javascript code that is needed for the component
        """
        return ''.join([element.render_js() for element in self.body()])

    def __str__(self) -> name:
        return self.name

    def __repr__(self) -> str:
        return f"Component('{self.name}')"
