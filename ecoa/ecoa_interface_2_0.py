from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional
from ecoa.ecoa_common_2_0 import Use

__NAMESPACE__ = "http://www.ecoa.technology/interface-2.0"


class EEventDirection(Enum):
    SENT_BY_PROVIDER = "SENT_BY_PROVIDER"
    RECEIVED_BY_PROVIDER = "RECEIVED_BY_PROVIDER"


@dataclass(repr=False)
class Operation:
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[A-Za-z][A-Za-z0-9_]*",
        }
    )
    comment: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(repr=False)
class Parameter:
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[A-Za-z][A-Za-z0-9_]*",
        }
    )
    type: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"([A-Za-z][A-Za-z0-9_\.]*:)?[A-Za-z][A-Za-z0-9_]*",
        }
    )


@dataclass(repr=False)
class Data(Operation):
    """
    Use of the "versioned data" exchange mechanism.
    """
    type: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"([A-Za-z][A-Za-z0-9_\.]*:)?[A-Za-z][A-Za-z0-9_]*",
        }
    )


@dataclass(repr=False)
class Event(Operation):
    """
    Use of the "event" exchange mechanism.
    """
    input: List[Parameter] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.ecoa.technology/interface-2.0",
        }
    )
    direction: Optional[EEventDirection] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass(repr=False)
class RequestResponse(Operation):
    """
    Use of the "request-response" exchange mechanism.
    """
    input: List[Parameter] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.ecoa.technology/interface-2.0",
        }
    )
    output: List[Parameter] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.ecoa.technology/interface-2.0",
        }
    )


@dataclass(repr=False)
class Operations:
    """
    A set of named operations.
    """
    data: List[Data] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.ecoa.technology/interface-2.0",
        }
    )
    event: List[Event] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.ecoa.technology/interface-2.0",
        }
    )
    requestresponse: List[RequestResponse] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.ecoa.technology/interface-2.0",
        }
    )


@dataclass(repr=False)
class ServiceDefinition1:
    """
    The definition of an ECOA service, including a set of operations.
    """
    class Meta:
        name = "ServiceDefinition"

    use: List[Use] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.ecoa.technology/interface-2.0",
        }
    )
    operations: Optional[Operations] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ecoa.technology/interface-2.0",
            "required": True,
        }
    )


@dataclass(repr=False)
class ServiceDefinition(ServiceDefinition1):
    class Meta:
        name = "serviceDefinition"
        namespace = "http://www.ecoa.technology/interface-2.0"
