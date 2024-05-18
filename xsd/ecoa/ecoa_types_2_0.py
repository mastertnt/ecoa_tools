from dataclasses import dataclass, field
from typing import List, Optional
from ecoa.ecoa_common_2_0 import Use

__NAMESPACE__ = "http://www.ecoa.technology/types-2.0"


@dataclass(unsafe_hash=True)
class Array:
    """
    Variable-size (bounded capacity) array.
    """
    item_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "itemType",
            "type": "Attribute",
            "required": True,
            "pattern": r"([A-Za-z][A-Za-z0-9_\.]*:)?[A-Za-z][A-Za-z0-9_]*",
        }
    )
    max_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "maxNumber",
            "type": "Attribute",
            "required": True,
            "pattern": r"%([A-Za-z][A-Za-z0-9_\.]*:)?[A-Za-z][A-Za-z0-9_]*%|[0-9]+",
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
    comment: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(unsafe_hash=True)
class Constant:
    """
    Constant definition.
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
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "length": 1,
            "pattern": r"%([A-Za-z][A-Za-z0-9_\.]*:)?[A-Za-z][A-Za-z0-9_]*%",
        }
    )
    comment: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(unsafe_hash=True)
class EnumValue:
    """
    A possible value of an enumerated type.
    """
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[A-Za-z][A-Za-z0-9_]*",
        }
    )
    valnum: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"%([A-Za-z][A-Za-z0-9_\.]*:)?[A-Za-z][A-Za-z0-9_]*%|(\+|-)?[0-9]*",
        }
    )
    comment: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(unsafe_hash=True)
class Field:
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
    comment: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(unsafe_hash=True)
class FixedArray:
    """
    Fixed-size array (size is always equal to max capacity)
    """
    item_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "itemType",
            "type": "Attribute",
            "required": True,
            "pattern": r"([A-Za-z][A-Za-z0-9_\.]*:)?[A-Za-z][A-Za-z0-9_]*",
        }
    )
    max_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "maxNumber",
            "type": "Attribute",
            "required": True,
            "pattern": r"%([A-Za-z][A-Za-z0-9_\.]*:)?[A-Za-z][A-Za-z0-9_]*%|[0-9]+",
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
    comment: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(unsafe_hash=True)
class Simple:
    """
    A type based on a predefined type (simple or E_basic) with a name, min/max
    constraints, and a unit.

    :ivar type:
    :ivar name:
    :ivar min_range:
    :ivar max_range:
    :ivar unit: Use of International System units is recommended.
    :ivar precision: Precision of values
    :ivar comment:
    """
    type: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"([A-Za-z][A-Za-z0-9_\.]*:)?[A-Za-z][A-Za-z0-9_]*",
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
    min_range: Optional[str] = field(
        default=None,
        metadata={
            "name": "minRange",
            "type": "Attribute",
            "length": 1,
            "pattern": r"%([A-Za-z][A-Za-z0-9_\.]*:)?[A-Za-z][A-Za-z0-9_]*%",
        }
    )
    max_range: Optional[str] = field(
        default=None,
        metadata={
            "name": "maxRange",
            "type": "Attribute",
            "length": 1,
            "pattern": r"%([A-Za-z][A-Za-z0-9_\.]*:)?[A-Za-z][A-Za-z0-9_]*%",
        }
    )
    unit: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    precision: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "length": 1,
            "pattern": r"%([A-Za-z][A-Za-z0-9_\.]*:)?[A-Za-z][A-Za-z0-9_]*%",
        }
    )
    comment: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(unsafe_hash=True)
class UnionType:
    class Meta:
        name = "Union"

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
    when: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    comment: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(unsafe_hash=True)
class EnumType:
    """
    Enumerated type.
    """
    class Meta:
        name = "Enum"

    value: List[EnumValue] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.ecoa.technology/types-2.0",
            "min_occurs": 1,
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
    type: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"([A-Za-z][A-Za-z0-9_\.]*:)?[A-Za-z][A-Za-z0-9_]*",
        }
    )
    comment: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(unsafe_hash=True)
class Record:
    """
    A record with named fields (Ada record, C struct)
    """
    field_value: List[Field] = field(
        default_factory=list,
        metadata={
            "name": "field",
            "type": "Element",
            "namespace": "http://www.ecoa.technology/types-2.0",
            "min_occurs": 1,
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
    comment: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(unsafe_hash=True)
class VariantRecord:
    """
    A record with variable parts: each "union" exists only if the selector has
    the value given by the "when" attribute.
    """
    field_value: List[Field] = field(
        default_factory=list,
        metadata={
            "name": "field",
            "type": "Element",
            "namespace": "http://www.ecoa.technology/types-2.0",
        }
    )
    union: List[UnionType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.ecoa.technology/types-2.0",
            "min_occurs": 1,
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
    select_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "selectName",
            "type": "Attribute",
            "required": True,
            "pattern": r"[A-Za-z][A-Za-z0-9_]*",
        }
    )
    select_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "selectType",
            "type": "Attribute",
            "required": True,
            "pattern": r"([A-Za-z][A-Za-z0-9_\.]*:)?[A-Za-z][A-Za-z0-9_]*",
        }
    )
    comment: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(unsafe_hash=True)
class DataTypes:
    """
    A set of data type definitions.
    """
    simple: List[Simple] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.ecoa.technology/types-2.0",
        }
    )
    record: List[Record] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.ecoa.technology/types-2.0",
        }
    )
    constant: List[Constant] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.ecoa.technology/types-2.0",
        }
    )
    variant_record: List[VariantRecord] = field(
        default_factory=list,
        metadata={
            "name": "variantRecord",
            "type": "Element",
            "namespace": "http://www.ecoa.technology/types-2.0",
        }
    )
    array: List[Array] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.ecoa.technology/types-2.0",
        }
    )
    fixed_array: List[FixedArray] = field(
        default_factory=list,
        metadata={
            "name": "fixedArray",
            "type": "Element",
            "namespace": "http://www.ecoa.technology/types-2.0",
        }
    )
    enum: List[EnumType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.ecoa.technology/types-2.0",
        }
    )


@dataclass(unsafe_hash=True)
class Library1:
    """
    A set of data types in a library.
    """
    class Meta:
        name = "Library"

    use: List[Use] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.ecoa.technology/types-2.0",
        }
    )
    types: Optional[DataTypes] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ecoa.technology/types-2.0",
            "required": True,
        }
    )


@dataclass(unsafe_hash=True)
class Library(Library1):
    class Meta:
        name = "library"
        namespace = "http://www.ecoa.technology/types-2.0"
