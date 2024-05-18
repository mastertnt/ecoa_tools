from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.ecoa.technology/types-2.0"


@dataclass(unsafe_hash=True)
class Use:
    """Declares the use of a library of data types.

    A type T defined in a library L will be denoted "L:T".
    """
    class Meta:
        name = "use"
        namespace = "http://www.ecoa.technology/types-2.0"

    library: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[A-Za-z][A-Za-z0-9_\.]*",
        }
    )
