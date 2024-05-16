from dataclasses import dataclass, field
from typing import List, Optional
from ecoa.ecoa_common_2_0 import (
    ProgrammingLanguage,
    Use,
)

__NAMESPACE__ = "http://www.ecoa.technology/implementation-2.0"


@dataclass(repr=False)
class Instance:
    """
    :ivar name:
    :ivar module_behaviour:
    :ivar relative_priority: Relative priority of this module instance
        to others module instances of the same component instance to
        help to distinguish them when allocating actual priorities at
        deployment level
    """
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[A-Za-z][A-Za-z0-9_]*",
        }
    )
    module_behaviour: Optional[str] = field(
        default=None,
        metadata={
            "name": "moduleBehaviour",
            "type": "Attribute",
        }
    )
    relative_priority: Optional[int] = field(
        default=None,
        metadata={
            "name": "relativePriority",
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0,
            "max_inclusive": 255,
        }
    )


@dataclass(repr=False)
class OpRef:
    """
    :ivar instance_name: Reference to a module instance, a service, or a
        reference
    :ivar operation_name:
    """
    instance_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "instanceName",
            "type": "Attribute",
            "required": True,
            "pattern": r"[A-Za-z][A-Za-z0-9_]*",
        }
    )
    operation_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "operationName",
            "type": "Attribute",
            "required": True,
            "pattern": r"[A-Za-z][A-Za-z0-9_]*",
        }
    )


@dataclass(repr=False)
class OpRefTrigger:
    """
    :ivar instance_name:
    :ivar period: period in seconds
    """
    class Meta:
        name = "OpRef_Trigger"

    instance_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "instanceName",
            "type": "Attribute",
            "required": True,
            "pattern": r"[A-Za-z][A-Za-z0-9_]*",
        }
    )
    period: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0.0,
        }
    )


@dataclass(repr=False)
class Parameter:
    """
    A parameter a an operation (Event, RequestResponse or VersionedData)
    """
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
class PinfoValue:
    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass(repr=False)
class PrivatePinfo:
    """
    Logical name of a private pinfo used by a module.
    """
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[A-Za-z][A-Za-z0-9_]*",
        }
    )


@dataclass(repr=False)
class PropertyValue:
    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass(repr=False)
class PublicPinfo:
    """
    Logical name of a public pinfo used by a module.
    """
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[A-Za-z][A-Za-z0-9_]*",
        }
    )


@dataclass(repr=False)
class ServiceQoS:
    """
    To define a new QoS for a provided or required service.
    """
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[A-Za-z][A-Za-z0-9_]*",
        }
    )
    new_qo_s: Optional[str] = field(
        default=None,
        metadata={
            "name": "newQoS",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass(repr=False)
class VersionedData:
    """
    :ivar name:
    :ivar type: Type stored by the versioned data.
    :ivar max_versions: Max number of versions accessed at the same
        time.
    """
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
    max_versions: int = field(
        default=1,
        metadata={
            "name": "maxVersions",
            "type": "Attribute",
        }
    )


@dataclass(repr=False)
class DynamicTriggerInstance(Instance):
    """
    :ivar parameter:
    :ivar size: Max number of events waiting for delay expiration in the
        trigger
    """
    parameter: List[Parameter] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.ecoa.technology/implementation-2.0",
        }
    )
    size: int = field(
        default=1,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(repr=False)
class Event:
    input: List[Parameter] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.ecoa.technology/implementation-2.0",
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[A-Za-z][A-Za-z0-9_]*",
        }
    )


@dataclass(repr=False)
class ModuleImplementation:
    """
    :ivar name:
    :ivar language: Programming language
    :ivar module_type:
    """
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[A-Za-z][A-Za-z0-9_]*",
        }
    )
    language: Optional[ProgrammingLanguage] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    module_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "moduleType",
            "type": "Attribute",
            "required": True,
            "pattern": r"[A-Za-z][A-Za-z0-9_]*",
        }
    )


@dataclass(repr=False)
class OpRefActivatable(OpRef):
    """
    :ivar activating: Does the reception of the event/data/rr cause the
        activation of the receiver module ?
    """
    activating: bool = field(
        default=True,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(repr=False)
class OpRefActivatingFifo(OpRef):
    """
    :ivar fifo_size: Max number of incoming operations that can be
        stored in the receiver module's FIFO queue for that particular
        operation link, before the activation of the corresponding
        entrypoint. There is one fifoSize per operation link on the
        receiver side. If this max number is exceeded, new incoming
        operations are discarded. These operations are activating.
    """
    fifo_size: int = field(
        default=8,
        metadata={
            "name": "fifoSize",
            "type": "Attribute",
        }
    )


@dataclass(repr=False)
class OpRefExternal:
    """
    Reference used for asynchronous notfication coming the legacy code (driver
    component)

    :ivar operation_name:
    :ivar language: Programming language in which the external API will
        be generated for the non-ECOA SW part of the driver component
    """
    class Meta:
        name = "OpRef_External"

    operation_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "operationName",
            "type": "Attribute",
            "required": True,
            "pattern": r"[A-Za-z][A-Za-z0-9_]*",
        }
    )
    language: Optional[ProgrammingLanguage] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass(repr=False)
class PropertyValues:
    """
    set of module property values.
    """
    property_value: List[PropertyValue] = field(
        default_factory=list,
        metadata={
            "name": "propertyValue",
            "type": "Element",
            "namespace": "http://www.ecoa.technology/implementation-2.0",
            "min_occurs": 1,
        }
    )


@dataclass(repr=False)
class RequestResponse:
    input: List[Parameter] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.ecoa.technology/implementation-2.0",
        }
    )
    output: List[Parameter] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.ecoa.technology/implementation-2.0",
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[A-Za-z][A-Za-z0-9_]*",
        }
    )


@dataclass(repr=False)
class TriggerInstance(Instance):
    pass


@dataclass(repr=False)
class ModuleInstance(Instance):
    """
    Describes an instance of a Module (having its own internal state).

    :ivar property_values:
    :ivar pinfo: Set of pinfo used by the module
    :ivar implementation_name:
    """
    property_values: Optional[PropertyValues] = field(
        default=None,
        metadata={
            "name": "propertyValues",
            "type": "Element",
            "namespace": "http://www.ecoa.technology/implementation-2.0",
        }
    )
    pinfo: Optional["ModuleInstance.Pinfo"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ecoa.technology/implementation-2.0",
        }
    )
    implementation_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "implementationName",
            "type": "Attribute",
            "required": True,
            "pattern": r"[A-Za-z][A-Za-z0-9_]*",
        }
    )

    @dataclass(repr=False)
    class Pinfo:
        public_pinfo: List[PinfoValue] = field(
            default_factory=list,
            metadata={
                "name": "publicPinfo",
                "type": "Element",
                "namespace": "http://www.ecoa.technology/implementation-2.0",
            }
        )
        private_pinfo: List[PinfoValue] = field(
            default_factory=list,
            metadata={
                "name": "privatePinfo",
                "type": "Element",
                "namespace": "http://www.ecoa.technology/implementation-2.0",
            }
        )


@dataclass(repr=False)
class ModuleType:
    """
    Describes a single-threaded ECOA module, implemented as software,
    contributing to the implementation of an ECOA component.

    :ivar properties: Set of module properties. The value of each module
        property is set at design time.
    :ivar pinfo: Set of pinfo used by the module
    :ivar operations:
    :ivar name:
    :ivar has_user_context: To indicate if the module relies on a user
        context
    :ivar has_warm_start_context: To indicate if the module relies on a
        warm start context
    :ivar is_fault_handler: To indicate if the module is a Fault Handler
        or not and to generate fault handling API. To enable the
        generation, the platform has to support this kind of Fault
        Handler deployment. See Platform Procurement Requirements.
    :ivar activating_fault_notifs: Does the reception of fault
        notifications cause the activation of the receiver Fault Handler
        (only if the Fault Handler is implemented as an ECOA component)
        ?
    """
    properties: Optional["ModuleType.Properties"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ecoa.technology/implementation-2.0",
        }
    )
    pinfo: Optional["ModuleType.Pinfo"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ecoa.technology/implementation-2.0",
        }
    )
    operations: Optional["ModuleType.Operations"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ecoa.technology/implementation-2.0",
            "required": True,
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[A-Za-z][A-Za-z0-9_]*",
        }
    )
    has_user_context: bool = field(
        default=True,
        metadata={
            "name": "hasUserContext",
            "type": "Attribute",
        }
    )
    has_warm_start_context: bool = field(
        default=True,
        metadata={
            "name": "hasWarmStartContext",
            "type": "Attribute",
        }
    )
    is_fault_handler: bool = field(
        default=False,
        metadata={
            "name": "isFaultHandler",
            "type": "Attribute",
        }
    )
    activating_fault_notifs: bool = field(
        default=True,
        metadata={
            "name": "activatingFaultNotifs",
            "type": "Attribute",
        }
    )

    @dataclass(repr=False)
    class Properties:
        """
        :ivar property: The value of each module property is set at
            design time at instance definition level.
        """
        property: List[Parameter] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://www.ecoa.technology/implementation-2.0",
                "min_occurs": 1,
            }
        )

    @dataclass(repr=False)
    class Pinfo:
        public_pinfo: List[PublicPinfo] = field(
            default_factory=list,
            metadata={
                "name": "publicPinfo",
                "type": "Element",
                "namespace": "http://www.ecoa.technology/implementation-2.0",
            }
        )
        private_pinfo: List[PrivatePinfo] = field(
            default_factory=list,
            metadata={
                "name": "privatePinfo",
                "type": "Element",
                "namespace": "http://www.ecoa.technology/implementation-2.0",
            }
        )

    @dataclass(repr=False)
    class Operations:
        """
        :ivar data_written: Read+Write access to a versioned data if
            writeonly=false. Write only access to a versioned data if
            writeonly=true. Note: the writeonly attribute is ignored by
            the Infrastructure if controlled=false on the dataLink.
        :ivar data_read: Read-only access to a versioned data.
        :ivar event_sent:
        :ivar event_received:
        :ivar request_sent:
        :ivar request_received:
        """
        data_written: List["ModuleType.Operations.DataWritten"] = field(
            default_factory=list,
            metadata={
                "name": "dataWritten",
                "type": "Element",
                "namespace": "http://www.ecoa.technology/implementation-2.0",
            }
        )
        data_read: List["ModuleType.Operations.DataRead"] = field(
            default_factory=list,
            metadata={
                "name": "dataRead",
                "type": "Element",
                "namespace": "http://www.ecoa.technology/implementation-2.0",
            }
        )
        event_sent: List[Event] = field(
            default_factory=list,
            metadata={
                "name": "eventSent",
                "type": "Element",
                "namespace": "http://www.ecoa.technology/implementation-2.0",
            }
        )
        event_received: List[Event] = field(
            default_factory=list,
            metadata={
                "name": "eventReceived",
                "type": "Element",
                "namespace": "http://www.ecoa.technology/implementation-2.0",
            }
        )
        request_sent: List["ModuleType.Operations.RequestSent"] = field(
            default_factory=list,
            metadata={
                "name": "requestSent",
                "type": "Element",
                "namespace": "http://www.ecoa.technology/implementation-2.0",
            }
        )
        request_received: List["ModuleType.Operations.RequestReceived"] = field(
            default_factory=list,
            metadata={
                "name": "requestReceived",
                "type": "Element",
                "namespace": "http://www.ecoa.technology/implementation-2.0",
            }
        )

        @dataclass(repr=False)
        class DataWritten(VersionedData):
            write_only: bool = field(
                default=False,
                metadata={
                    "name": "writeOnly",
                    "type": "Attribute",
                }
            )

        @dataclass(repr=False)
        class DataRead(VersionedData):
            notifying: bool = field(
                default=False,
                metadata={
                    "type": "Attribute",
                }
            )

        @dataclass(repr=False)
        class RequestSent(RequestResponse):
            """
            :ivar timeout: Timeout value to unblock/inform respectively
                a synchronous/asynchronous RR If the value is negative,
                the timeout is infinite.
            :ivar is_synchronous:
            :ivar max_concurrent_requests: Max number of concurrent
                requests that the module may handle for the related
                container call.
            """
            timeout: Optional[float] = field(
                default=None,
                metadata={
                    "type": "Attribute",
                    "required": True,
                }
            )
            is_synchronous: Optional[bool] = field(
                default=None,
                metadata={
                    "name": "isSynchronous",
                    "type": "Attribute",
                    "required": True,
                }
            )
            max_concurrent_requests: int = field(
                default=10,
                metadata={
                    "name": "maxConcurrentRequests",
                    "type": "Attribute",
                }
            )

        @dataclass(repr=False)
        class RequestReceived(RequestResponse):
            """
            :ivar max_concurrent_requests: Max number of concurrent
                responses that the module may handle for the related
                entry-point, regardless of incoming requestLinks related
                to that entry-point.
            """
            max_concurrent_requests: int = field(
                default=10,
                metadata={
                    "name": "maxConcurrentRequests",
                    "type": "Attribute",
                }
            )


@dataclass(repr=False)
class OpRefActivatableFifo(OpRefActivatable):
    """
    :ivar fifo_size: Max number of incoming operations that can be
        stored in the receiver module's FIFO queue for that particular
        operation link, before the activation of the corresponding
        entrypoint. There is one fifoSize per operation link on the
        receiver side. If this max number is exceeded, new incoming
        operations are trashed.
    """
    fifo_size: int = field(
        default=8,
        metadata={
            "name": "fifoSize",
            "type": "Attribute",
        }
    )


@dataclass(repr=False)
class DataLink:
    """
    Link between DATA operations.

    :ivar writers:
    :ivar readers:
    :ivar id:
    :ivar controlled: Boolean flag to indicate if the Versioned Data
        access are controlled by the Infrastructure. If true, each
        concurrent write accesses to its own copy of the data and
        readers are ensured that the copy they access is stable until
        the release of the VD handle. Otherwise, if false, any module
        getting a handle may directly access the local data repository
        (as no copy is made by the Infrastructure).
    """
    writers: Optional["DataLink.Writers"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ecoa.technology/implementation-2.0",
            "required": True,
        }
    )
    readers: Optional["DataLink.Readers"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ecoa.technology/implementation-2.0",
        }
    )
    id: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    controlled: bool = field(
        default=True,
        metadata={
            "type": "Attribute",
        }
    )

    @dataclass(repr=False)
    class Writers:
        reference: List[OpRef] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://www.ecoa.technology/implementation-2.0",
                "sequential": True,
            }
        )
        module_instance: List[OpRef] = field(
            default_factory=list,
            metadata={
                "name": "moduleInstance",
                "type": "Element",
                "namespace": "http://www.ecoa.technology/implementation-2.0",
                "sequential": True,
            }
        )

    @dataclass(repr=False)
    class Readers:
        service: List[OpRef] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://www.ecoa.technology/implementation-2.0",
                "sequential": True,
            }
        )
        module_instance: List[OpRefActivatableFifo] = field(
            default_factory=list,
            metadata={
                "name": "moduleInstance",
                "type": "Element",
                "namespace": "http://www.ecoa.technology/implementation-2.0",
                "sequential": True,
            }
        )


@dataclass(repr=False)
class EventLink:
    """
    Link between EVENT operations.
    """
    senders: Optional["EventLink.Senders"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ecoa.technology/implementation-2.0",
        }
    )
    receivers: Optional["EventLink.Receivers"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ecoa.technology/implementation-2.0",
            "required": True,
        }
    )
    id: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )

    @dataclass(repr=False)
    class Senders:
        service: List[OpRef] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://www.ecoa.technology/implementation-2.0",
                "sequential": True,
            }
        )
        reference: List[OpRef] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://www.ecoa.technology/implementation-2.0",
                "sequential": True,
            }
        )
        module_instance: List[OpRef] = field(
            default_factory=list,
            metadata={
                "name": "moduleInstance",
                "type": "Element",
                "namespace": "http://www.ecoa.technology/implementation-2.0",
                "sequential": True,
            }
        )
        trigger: List[OpRefTrigger] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://www.ecoa.technology/implementation-2.0",
                "sequential": True,
            }
        )
        dynamic_trigger: List[OpRef] = field(
            default_factory=list,
            metadata={
                "name": "dynamicTrigger",
                "type": "Element",
                "namespace": "http://www.ecoa.technology/implementation-2.0",
                "sequential": True,
            }
        )
        external: List[OpRefExternal] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://www.ecoa.technology/implementation-2.0",
                "sequential": True,
            }
        )

    @dataclass(repr=False)
    class Receivers:
        service: List[OpRef] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://www.ecoa.technology/implementation-2.0",
                "sequential": True,
            }
        )
        reference: List[OpRef] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://www.ecoa.technology/implementation-2.0",
                "sequential": True,
            }
        )
        module_instance: List[OpRefActivatableFifo] = field(
            default_factory=list,
            metadata={
                "name": "moduleInstance",
                "type": "Element",
                "namespace": "http://www.ecoa.technology/implementation-2.0",
                "sequential": True,
            }
        )
        dynamic_trigger: List[OpRefActivatingFifo] = field(
            default_factory=list,
            metadata={
                "name": "dynamicTrigger",
                "type": "Element",
                "namespace": "http://www.ecoa.technology/implementation-2.0",
                "sequential": True,
            }
        )


@dataclass(repr=False)
class RequestLink:
    """Link between RR operations.

    Must have exactly one server. Can have many clients.
    """
    clients: Optional["RequestLink.Clients"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ecoa.technology/implementation-2.0",
            "required": True,
        }
    )
    server: Optional["RequestLink.Server"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ecoa.technology/implementation-2.0",
            "required": True,
        }
    )
    id: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )

    @dataclass(repr=False)
    class Clients:
        """
        :ivar service:
        :ivar module_instance: Note: attribute 'activating' concerns the
            response, and is applicable to asynchronous RR operations
            only.
        """
        service: List[OpRef] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://www.ecoa.technology/implementation-2.0",
                "sequential": True,
            }
        )
        module_instance: List[OpRefActivatable] = field(
            default_factory=list,
            metadata={
                "name": "moduleInstance",
                "type": "Element",
                "namespace": "http://www.ecoa.technology/implementation-2.0",
                "sequential": True,
            }
        )

    @dataclass(repr=False)
    class Server:
        """
        :ivar reference:
        :ivar module_instance: Note: optional attributes concern the
            request
        """
        reference: Optional[OpRef] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.ecoa.technology/implementation-2.0",
            }
        )
        module_instance: Optional[OpRefActivatableFifo] = field(
            default=None,
            metadata={
                "name": "moduleInstance",
                "type": "Element",
                "namespace": "http://www.ecoa.technology/implementation-2.0",
            }
        )


@dataclass(repr=False)
class ComponentImplementation1:
    """
    Describes all the information needed to integrate the software
    implementation of an ECOA component in an ECOA system.
    """
    class Meta:
        name = "ComponentImplementation"

    use: List[Use] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.ecoa.technology/implementation-2.0",
        }
    )
    service: List[ServiceQoS] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.ecoa.technology/implementation-2.0",
        }
    )
    reference: List[ServiceQoS] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.ecoa.technology/implementation-2.0",
        }
    )
    module_type: List[ModuleType] = field(
        default_factory=list,
        metadata={
            "name": "moduleType",
            "type": "Element",
            "namespace": "http://www.ecoa.technology/implementation-2.0",
        }
    )
    module_implementation: List[ModuleImplementation] = field(
        default_factory=list,
        metadata={
            "name": "moduleImplementation",
            "type": "Element",
            "namespace": "http://www.ecoa.technology/implementation-2.0",
        }
    )
    module_instance: List[ModuleInstance] = field(
        default_factory=list,
        metadata={
            "name": "moduleInstance",
            "type": "Element",
            "namespace": "http://www.ecoa.technology/implementation-2.0",
        }
    )
    trigger_instance: List[TriggerInstance] = field(
        default_factory=list,
        metadata={
            "name": "triggerInstance",
            "type": "Element",
            "namespace": "http://www.ecoa.technology/implementation-2.0",
        }
    )
    dynamic_trigger_instance: List[DynamicTriggerInstance] = field(
        default_factory=list,
        metadata={
            "name": "dynamicTriggerInstance",
            "type": "Element",
            "namespace": "http://www.ecoa.technology/implementation-2.0",
        }
    )
    data_link: List[DataLink] = field(
        default_factory=list,
        metadata={
            "name": "dataLink",
            "type": "Element",
            "namespace": "http://www.ecoa.technology/implementation-2.0",
            "sequential": True,
        }
    )
    event_link: List[EventLink] = field(
        default_factory=list,
        metadata={
            "name": "eventLink",
            "type": "Element",
            "namespace": "http://www.ecoa.technology/implementation-2.0",
            "sequential": True,
        }
    )
    request_link: List[RequestLink] = field(
        default_factory=list,
        metadata={
            "name": "requestLink",
            "type": "Element",
            "namespace": "http://www.ecoa.technology/implementation-2.0",
            "sequential": True,
        }
    )
    component_definition: Optional[str] = field(
        default=None,
        metadata={
            "name": "componentDefinition",
            "type": "Attribute",
            "required": True,
            "pattern": r"[A-Za-z][A-Za-z0-9_]*",
        }
    )


@dataclass(repr=False)
class ComponentImplementation(ComponentImplementation1):
    class Meta:
        name = "componentImplementation"
        namespace = "http://www.ecoa.technology/implementation-2.0"
