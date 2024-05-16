from dataclasses import dataclass, field
from typing import List, Optional
from ecoa.ecoa_sca import Interface as EcoaScaInterface

__NAMESPACE__ = "http://docs.oasis-open.org/ns/opencsa/sca/200912"


@dataclass(repr=False)
class Interface:
    class Meta:
        name = "interface"

    interface: Optional[EcoaScaInterface] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ecoa.technology/sca-extension-2.0",
            "required": True,
        }
    )


@dataclass(repr=False)
class Reference(Interface):
    class Meta:
        name = "reference"
        namespace = "http://docs.oasis-open.org/ns/opencsa/sca/200912"

    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass(repr=False)
class Service(Interface):
    class Meta:
        name = "service"
        namespace = "http://docs.oasis-open.org/ns/opencsa/sca/200912"

    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass(repr=False)
class ComponentType:
    class Meta:
        name = "componentType"
        namespace = "http://docs.oasis-open.org/ns/opencsa/sca/200912"

    service: List[Service] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    reference: List[Reference] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
