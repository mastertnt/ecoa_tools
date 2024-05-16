from dataclasses import dataclass, field
from typing import List, Optional


@dataclass(repr=False)
class ContainerGenerator:
    output: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    generate_sub_directory: Optional[bool] = field(
        default=None,
        metadata={
            "name": "generateSubDirectory",
            "type": "Attribute",
        }
    )
    generate_directory_for_component: Optional[bool] = field(
        default=None,
        metadata={
            "name": "generateDirectoryForComponent",
            "type": "Attribute",
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(repr=False)
class EcoaGenericPlatformGenerator:
    output: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    sub_directory: Optional[str] = field(
        default=None,
        metadata={
            "name": "subDirectory",
            "type": "Attribute",
        }
    )
    context: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(repr=False)
class ModuleGenerator:
    output: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    generate_inc: Optional[bool] = field(
        default=None,
        metadata={
            "name": "generateInc",
            "type": "Attribute",
        }
    )
    generate_directory_for_component: Optional[bool] = field(
        default=None,
        metadata={
            "name": "generateDirectoryForComponent",
            "type": "Attribute",
        }
    )


@dataclass(repr=False)
class TypeGenerator:
    output: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    generate_inc: Optional[bool] = field(
        default=None,
        metadata={
            "name": "generateInc",
            "type": "Attribute",
        }
    )
    seperate_library: Optional[bool] = field(
        default=None,
        metadata={
            "name": "seperateLibrary",
            "type": "Attribute",
        }
    )


@dataclass(repr=False)
class GeneratorConfiguration:
    type_generator: Optional[TypeGenerator] = field(
        default=None,
        metadata={
            "name": "TypeGenerator",
            "type": "Element",
        }
    )
    module_generator: Optional[ModuleGenerator] = field(
        default=None,
        metadata={
            "name": "ModuleGenerator",
            "type": "Element",
        }
    )
    container_generator: List[ContainerGenerator] = field(
        default_factory=list,
        metadata={
            "name": "ContainerGenerator",
            "type": "Element",
        }
    )
    ecoa_generic_platform_generator: Optional[EcoaGenericPlatformGenerator] = field(
        default=None,
        metadata={
            "name": "EcoaGenericPlatformGenerator",
            "type": "Element",
        }
    )
