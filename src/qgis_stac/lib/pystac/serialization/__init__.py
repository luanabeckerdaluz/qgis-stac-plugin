__all__ = [
    "merge_common_properties",
    "migrate_to_latest",
    "STACVersionRange",
    "identify_stac_object",
    "identify_stac_object_type",
]
from ..serialization.identify import (
    STACVersionRange,
    identify_stac_object,
    identify_stac_object_type,
)
from ..serialization.common_properties import merge_common_properties
from ..serialization.migrate import migrate_to_latest
