from typing import Any, Optional, Union

from lxml.etree import ElementBase, XMLParser

# dummy for missing stubs
def __getattr__(name) -> Any: ...

class ObjectifiedElement(ElementBase):
    def __getattr__(self, name) -> ObjectifiedElement: ...

def fromstring(
    text: Union[bytes, str],
    parser: XMLParser = ...,
    *,
    base_url: Optional[Union[bytes, str]] = ...
) -> ObjectifiedElement: ...
