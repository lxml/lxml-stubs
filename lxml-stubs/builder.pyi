from typing import Any, Callable, Mapping, Optional, Protocol, TypeVar, Union

from lxml.etree import _Element, _NSMapArg, _TagName, CDATA

type _Child = Union[_Element, str, CDATA, dict[str, str]]

_T = TypeVar("_T")

class _MakeElement(Protocol):
    def __call__(
        self, __tag: _TagName, *, nsmap: Optional[_NSMapArg] = None
    ) -> _Element: ...

class _TaggedElementMaker(Protocol):
    def __call__(self, *children: _Child, **attrib: str) -> _Element: ...

class ElementMaker:
    def __init__(
        self,
        typemap: Optional[Mapping[type[_T], Callable[[_Element, _T], Any]]] = None,
        namespace: Optional[str] = None,
        nsmap: Optional[_NSMapArg] = None,
        makeelement: Optional[_MakeElement] = None,
    ): ...
    def __call__(self, tag: _TagName, *children: _Child, **attrib: str) -> _Element: ...
    def __getattr__(self, tag: _TagName) -> _TaggedElementMaker: ...

E = ElementMaker()
