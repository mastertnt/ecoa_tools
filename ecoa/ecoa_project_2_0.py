from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "http://www.ecoa.technology/project-2.0"


@dataclass(repr=False)
class EliEuids:
    """
    List of bindings.
    """
    class Meta:
        name = "ELI_EUIDs"

    euid: List[str] = field(
        default_factory=list,
        metadata={
            "name": "EUID",
            "type": "Element",
            "namespace": "http://www.ecoa.technology/project-2.0",
            "min_occurs": 1,
        }
    )


@dataclass(repr=False)
class Files:
    """
    List of files.
    """
    file: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.ecoa.technology/project-2.0",
            "min_occurs": 1,
        }
    )


@dataclass(repr=False)
class EcoaProject1:
    """
    Describes a whole ECOA project.
    """
    class Meta:
        name = "EcoaProject"

    service_definitions: List[Files] = field(
        default_factory=list,
        metadata={
            "name": "serviceDefinitions",
            "type": "Element",
            "namespace": "http://www.ecoa.technology/project-2.0",
            "sequential": True,
        }
    )
    component_definitions: List[Files] = field(
        default_factory=list,
        metadata={
            "name": "componentDefinitions",
            "type": "Element",
            "namespace": "http://www.ecoa.technology/project-2.0",
            "sequential": True,
        }
    )
    types: List[Files] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.ecoa.technology/project-2.0",
            "sequential": True,
        }
    )
    initial_assembly: List[str] = field(
        default_factory=list,
        metadata={
            "name": "initialAssembly",
            "type": "Element",
            "namespace": "http://www.ecoa.technology/project-2.0",
            "sequential": True,
        }
    )
    component_implementations: List[Files] = field(
        default_factory=list,
        metadata={
            "name": "componentImplementations",
            "type": "Element",
            "namespace": "http://www.ecoa.technology/project-2.0",
            "sequential": True,
        }
    )
    logical_system: List[str] = field(
        default_factory=list,
        metadata={
            "name": "logicalSystem",
            "type": "Element",
            "namespace": "http://www.ecoa.technology/project-2.0",
            "sequential": True,
        }
    )
    cross_platforms_view: List[str] = field(
        default_factory=list,
        metadata={
            "name": "crossPlatformsView",
            "type": "Element",
            "namespace": "http://www.ecoa.technology/project-2.0",
            "sequential": True,
        }
    )
    deployment_schema: List[str] = field(
        default_factory=list,
        metadata={
            "name": "deploymentSchema",
            "type": "Element",
            "namespace": "http://www.ecoa.technology/project-2.0",
            "sequential": True,
        }
    )
    output_directory: List[str] = field(
        default_factory=list,
        metadata={
            "name": "outputDirectory",
            "type": "Element",
            "namespace": "http://www.ecoa.technology/project-2.0",
            "sequential": True,
        }
    )
    implementation_assembly: List[str] = field(
        default_factory=list,
        metadata={
            "name": "implementationAssembly",
            "type": "Element",
            "namespace": "http://www.ecoa.technology/project-2.0",
            "sequential": True,
        }
    )
    euids: List[EliEuids] = field(
        default_factory=list,
        metadata={
            "name": "EUIDs",
            "type": "Element",
            "namespace": "http://www.ecoa.technology/project-2.0",
            "sequential": True,
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
class Ecoaproject(EcoaProject1):
    class Meta:
        name = "ECOAProject"
        namespace = "http://www.ecoa.technology/project-2.0"
