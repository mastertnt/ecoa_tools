from dataclasses import dataclass, field
from typing import List, Optional


@dataclass(repr=False)
class ContainerGenerator:
    output: Optional[str] = field(
        default=".",
        metadata={
            "type": "Attribute",
        }
    )
    generateSubDirectory: Optional[bool] = field(
        default=False,
        metadata={
            "type": "Attribute",
        }
    )
    generateDirectoryPerComponent: Optional[bool] = field(
        default=False,
        metadata={
            "type": "Attribute",
        }
    )
    name: str = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(repr=False)
class TestsGenerator:
    output: Optional[str] = field(
        default=".",
        metadata={
            "type": "Attribute",
        }
    )
    generateSubDirectory: Optional[bool] = field(
        default=False,
        metadata={
            "type": "Attribute",
        }
    )
    name: str = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(repr=False)
class ModuleGenerator:
    output: Optional[str] = field(
        default=".",
        metadata={
            "type": "Attribute",
        }
    )
    generateSubDirectory: Optional[bool] = field(
        default=False,
        metadata={
            "type": "Attribute",
        }
    )
    generateDirectoryPerComponent: Optional[bool] = field(
        default=False,
        metadata={
            "type": "Attribute",
        }
    )
    name: str = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(repr=False)
class TypeGenerator:
    output: Optional[str] = field(
        default=".",
        metadata={
            "type": "Attribute",
        }
    )
    generateSubDirectory: Optional[bool] = field(
        default=False,
        metadata={
            "type": "Attribute",
        }
    )
    generateDirectoryPerLibrary: Optional[bool] = field(
        default=False,
        metadata={
            "type": "Attribute",
        }
    )
    name: str = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(repr=False)
class GeneratorConfiguration:
    type_generator: List[TypeGenerator] = field(
        default=None,
        metadata={
            "name": "TypeGenerator",
            "type": "Element",
        }
    )
    module_generator: List[ModuleGenerator] = field(
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
    ecoa_tests_generator: List[TestsGenerator] = field(
        default=None,
        metadata={
            "name": "TestsGenerator",
            "type": "Element",
        }
    )
