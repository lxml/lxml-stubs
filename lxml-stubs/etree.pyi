# Hand-written stub for lxml.etree as used by mypy.report.
# This is *far* from complete, and the stubgen-generated ones crash mypy.
# Any use of `Any` below means I couldn't figure out the type.

from typing import (
    Any,
    Dict,
    IO,
    Iterable,
    Iterator,
    List,
    Mapping,
    Tuple,
    Union,
    Optional,
    Sequence,
    Sized,
    SupportsBytes,
    TypeVar,
    overload,
)

from typing_extensions import Protocol


# dummy for missing stubs
def __getattr__(name: str) -> Any: ...

# We do *not* want `typing.AnyStr` because it is a `TypeVar`, which is an
# unnecessary constraint. It seems reasonable to constrain each
# List/Dict argument to use one type consistently, though, and it is
# necessary in order to keep these brief.
_AnyStr = Union[str, bytes]
_AnySmartStr = Union['_ElementUnicodeResult', '_PyElementUnicodeResult', '_ElementStringResult']
# XPath object - http://lxml.de/xpathxslt.html#xpath-return-values
_XPathObject = Union[bool, float, _AnySmartStr, _AnyStr, List[Union['_Element', _AnySmartStr, _AnyStr, Tuple[Optional[_AnyStr], Optional[_AnyStr]]]]]
_ListAnyStr = Union[List[str], List[bytes]]
_DictAnyStr = Union[Dict[str, str], Dict[bytes, bytes]]
_Dict_Tuple2AnyStr_Any = Union[Dict[Tuple[str, str], Any], Tuple[bytes, bytes], Any]
_NSMap = Union[Dict[Union[bytes, None], bytes], Dict[Union[str, None], str]]
_xpath = Union['XPath', _AnyStr]
_OptionalNamespace = Optional[Mapping[str, Any]]
_T = TypeVar('_T') 

class ElementChildIterator(Iterator['_Element']):
    def __iter__(self) -> 'ElementChildIterator': ...
    def __next__(self) -> '_Element': ...

class _ElementUnicodeResult(str):
    is_attribute: bool
    is_tail: bool
    is_text: bool
    attrname: Optional[_AnyStr]
    def getparent(self) -> Optional['_Element']: ...

class _PyElementUnicodeResult(str):
    is_attribute: bool
    is_tail: bool
    is_text: bool
    attrname: Optional[_AnyStr]
    def getparent(self) -> Optional['_Element']: ...

class _ElementStringResult(bytes):
    is_attribute: bool
    is_tail: bool
    is_text: bool
    attrname: Optional[_AnyStr]
    def getparent(self) -> Optional['_Element']: ...

class _Element(Iterable['_Element'], Sized):
    def __delitem__(self, key: Union[int, slice]) -> None: ...
    def __getitem__(self, item: int) -> _Element: ...
    def __len__(self) -> int: ...
    def addprevious(self, element: '_Element') -> None: ...
    def addnext(self, element: '_Element') -> None: ...
    def append(self, element: '_Element') -> None: ...
    def cssselect(self, expression: str) -> List[_Element]: ...
    def find(self, path: str, namespace: _OptionalNamespace = ...) -> Optional['_Element']: ...
    def findall(self,
                name: str,
                namespace: _OptionalNamespace = ...) -> List['_Element']: ...
    def clear(self) -> None: ...
    @overload
    def get(self, key: _AnyStr) -> Optional[_AnyStr]: ...
    @overload
    def get(self, key: _AnyStr, default: _T) -> Union[_AnyStr, _T]: ...
    def getnext(self) -> Optional[_Element]: ...
    def getparent(self) -> Optional[_Element]: ...
    def getprevious(self) -> Optional[_Element]: ...
    def getroottree(self) -> _ElementTree: ...
    def insert(self, index: int, element: _Element) -> None: ...
    def iter(self,
             tag: Optional[_AnyStr] = ...,
             *tags: _AnyStr) -> Iterable[_Element]: ...
    def makeelement(self,
                    _tag: Union[_AnyStr, QName],
                    attrib: Optional[_DictAnyStr] = ...,
                    nsmap: Optional[_NSMap] = ...,
                    **_extra: Any
                    ) -> _Element: ...
    def remove(self, element: _Element) -> None: ...
    def xpath(self,
              _path: _AnyStr,
              namespaces: Optional[_DictAnyStr] = ...,
              extensions: Any = ...,
              smart_strings: bool = ...,
              **_variables: _XPathObject) -> _XPathObject: ...
    attrib = ...  # type: _Attrib
    text = ...  # type: Optional[_AnyStr]
    tag = ...  # type: Union[_AnyStr, QName]
    tail = ...  # type: Optional[_AnyStr]
    nsmap = ...  # type: _NSMap
    def __iter__(self) -> ElementChildIterator: ...
    def items(self) -> Sequence[Tuple[_AnyStr, _AnyStr]]: ...
    def iterfind(self, path: str, namespace: _OptionalNamespace = None)  -> Iterator['_Element']: ...

class ElementBase(_Element): ...

class _ElementTree:
    parser = ... # type: XMLParser
    def getpath(self, element: _Element) -> str: ...
    def getroot(self) -> _Element: ...
    def write(self,
              file: Union[_AnyStr, IO[Any]],
              encoding: _AnyStr = ...,
              method: _AnyStr = ...,
              pretty_print: bool = ...,
              xml_declaration: Any = ...,
              with_tail: Any = ...,
              standalone: bool = ...,
              compression: int = ...,
              exclusive: bool = ...,
              with_comments: bool = ...,
              inclusive_ns_prefixes: _ListAnyStr = ...) -> None: ...
    def write_c14n(self,
                   file: Union[_AnyStr, IO[Any]],
                   with_comments: bool = ...,
                   compression: int = ...,
                   inclusive_ns_prefixes: Iterable[_AnyStr] = ...) -> None: ...
    def _setroot(self, root: _Element) -> None: ...
    def xpath(self,
              _path: _AnyStr,
              namespaces: Optional[_DictAnyStr] = ...,
              extensions: Any = ...,
              smart_strings: bool = ...,
              **_variables: _XPathObject) -> _XPathObject: ...
    def xslt(self,
             _xslt: XSLT,
             extensions: Optional[_Dict_Tuple2AnyStr_Any] = ...,
             access_control: Optional[XSLTAccessControl] = ...,
             **_variables: Any) -> _ElementTree: ...


class __ContentOnlyEleement(_Element): ...


class _Comment(__ContentOnlyEleement): ...


class _ProcessingInstruction(__ContentOnlyEleement):
    target: _AnyStr


class _Attrib:
    def __setitem__(self, key: _AnyStr, value: _AnyStr) -> None :...
    def __delitem__(self, key: _AnyStr) -> None: ...
    def update(self,
               sequence_or_dict: Union[Sequence[Tuple[_AnyStr, _AnyStr]],
                                       Mapping[_AnyStr, _AnyStr]]) -> None: ...
    def pop(self, key: _AnyStr, default: _AnyStr) -> _AnyStr: ...
    def clear(self) -> None: ...
    def __repr__(self) -> str: ...
    def __copy__(self) -> _DictAnyStr: ...
    def __deepcopy__(self, memo: Dict[Any, Any]) -> _DictAnyStr: ...
    def __getitem__(self, key: _AnyStr) -> _AnyStr: ...
    def __bool__(self) -> bool: ...
    def __len__(self) -> int: ...
    def get(self, key: _AnyStr, default: _AnyStr = ...) -> Optional[_AnyStr]: ...
    def keys(self) -> _ListAnyStr: ...
    def __iter__(self) -> Iterator[_AnyStr]: ...  # actually _AttribIterator
    def iterkeys(self) -> Iterator[_AnyStr]: ...
    def values(self) -> _ListAnyStr: ...
    def itervalues(self) -> Iterator[_AnyStr]: ...
    def items(self) -> List[Tuple[_AnyStr, _AnyStr]]: ...
    def iteritems(self) -> Iterator[Tuple[_AnyStr, _AnyStr]]: ...
    def has_key(self, key: _AnyStr) -> bool: ...
    def __contains__(self, key: _AnyStr) -> bool: ...
    def __richcmp__(self, other: _Attrib, op: int) -> bool: ...


class QName:
    localname = ... # type: _AnyStr
    namespace = ... # type: _AnyStr
    text = ... # type: _AnyStr
    def __init__(self,
                 text_or_uri_element: Union[None, _AnyStr, _Element],
                 tag: Optional[_AnyStr] = ...) -> None: ...

class _XSLTResultTree(_ElementTree, SupportsBytes):
    def __bytes__(self) -> bytes: ...

class _XSLTQuotedStringParam: ...


# https://lxml.de/parsing.html#the-target-parser-interface
class ParserTarget(Protocol):
    def comment(self, text: _AnyStr) -> None: ...
    def close(self) -> Any: ...
    def data(self, data: _AnyStr) -> None: ...
    def end(self, tag: _AnyStr) -> None: ...
    def start(self, tag: _AnyStr, attrib: _DictAnyStr) -> None: ...

class XMLParser:
    def __init__(self,
                 encoding: Optional[_AnyStr] = ...,
                 attribute_defaults: bool = ...,
                 dtd_validation: bool = ...,
                 load_dtd: bool = ...,
                 no_network: bool = ...,
                 ns_clean: bool = ...,
                 recover: bool = ...,
                 schema: Optional[XMLSchema] = ...,
                 huge_tree: bool = ...,
                 remove_blank_text: bool = ...,
                 resolve_entities: bool = ...,
                 remove_comments: bool = ...,
                 remove_pis: bool = ...,
                 strip_cdata: bool = ...,
                 collect_ids: bool = ...,
                 target: Optional[ParserTarget] = ...,
                 compact: bool = ...) -> None: ...

class XMLSchema:
    def __init__(self,
                 etree: Union[_Element, _ElementTree] = ...,
                 file: Union[_AnyStr, IO[Any]] = ...) -> None: ...
    def assertValid(self, etree: Union[_Element, _ElementTree]) -> None: ...

class XSLTAccessControl: ...

class XSLT:
    def __init__(self,
                 xslt_input: Union[_Element, _ElementTree],
                 extensions: _Dict_Tuple2AnyStr_Any = ...,
                 regexp: bool = ...,
                 access_control: XSLTAccessControl = ...) -> None: ...
    def __call__(self,
                 _input: Union[_Element, _ElementTree],
                 profile_run: bool = ...,
                 **kwargs: Union[_AnyStr, _XSLTQuotedStringParam]) -> _XSLTResultTree: ...
    @staticmethod
    def strparam(s: _AnyStr) -> _XSLTQuotedStringParam: ...


def Comment(text: Optional[_AnyStr] = ...) -> _Comment: ...

def Element(_tag: _AnyStr,
            attrib: Optional[_DictAnyStr] = ...,
            nsmap: Optional[_NSMap] = ...,
            **extra: _AnyStr) -> _Element: ...
def SubElement(_parent: _Element, _tag: _AnyStr,
               attrib: Optional[_DictAnyStr] = ...,
               nsmap: Optional[_NSMap] = ...,
               **extra: _AnyStr) -> _Element: ...
def ElementTree(element: _Element = ...,
                file: Union[_AnyStr, IO[Any]] = ...,
                parser: XMLParser = ...) -> _ElementTree: ...
def ProcessingInstruction(
        target: _AnyStr,
        text: _AnyStr = ...
) -> _ProcessingInstruction: ...

PI = ProcessingInstruction

def cleanup_namespaces(tree_or_element: Union[_Element, _ElementTree],
                       top_nsmap: Optional[_NSMap] = ...,
                       keep_ns_prefixes: Optional[Iterable[_AnyStr]] = ...) -> None: ...

def parse(source: Union[_AnyStr, IO[Any]],
          parser: XMLParser = ...,
          base_url: _AnyStr = ...) -> _ElementTree: ...
def fromstring(text: _AnyStr,
               parser: XMLParser = ...,
               *,
               base_url: _AnyStr = ...) -> _Element: ...
def tostring(element_or_tree: Union[_Element, _ElementTree],
             encoding: Union[str, type] = ...,
             method: str = ...,
             xml_declaration: bool = ...,
             pretty_print: bool = ...,
             with_tail: bool = ...,
             standalone: bool = ...,
             doctype: str = ...,
             exclusive: bool = ...,
             with_comments: bool = ...,
             inclusive_ns_prefixes: Any = ...) -> _AnyStr: ...

class _ErrorLog: ...

class Error(Exception): ...

class LxmlError(Error):
    def __init__(self, message: Any, error_log: _ErrorLog = ...) -> None: ...
    error_log = ...  # type: _ErrorLog

class DocumentInvalid(LxmlError): ...
class LxmlSyntaxError(LxmlError, SyntaxError): ...
class ParseError(LxmlSyntaxError): ...
class XMLSyntaxError(ParseError): ...

class _Validator: ...

class DTD(_Validator):
    def __init__(self,
                 file: Union[_AnyStr, IO[Any]] = ...,
                 *,
                 external_id: Any = ...) -> None: ...

    def assertValid(self, etree: _Element) -> None: ...

class XPath:
    def __init__(self,
                 path: _AnyStr,
                 *,
                 namespaces: Optional[_AnyStr] = ...,
                 extensions: Optional[_AnyStr] = ...,
                 regexp: bool = ...,
                 smart_strings: bool = ...) -> None: ...
    def __call__(self, _etree_or_element: Union[_Element, _ElementTree], **_variables: _XPathObject) -> _XPathObject: ...
