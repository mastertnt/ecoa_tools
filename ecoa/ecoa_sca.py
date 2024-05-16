from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.ecoa.technology/sca-extension-2.0"


@dataclass(repr=False)
class Interface:
    class Meta:
        name = "interface"
        namespace = "http://www.ecoa.technology/sca-extension-2.0"

    syntax: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
