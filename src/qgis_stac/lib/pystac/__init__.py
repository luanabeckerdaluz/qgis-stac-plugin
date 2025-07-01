"""
PySTAC is a library for working with SpatioTemporal Asset Catalogs (STACs)
"""
__all__ = [
    "__version__",
    "STACError",
    "STACTypeError",
    "DuplicateObjectKeyError",
    "ExtensionAlreadyExistsError",
    "ExtensionNotImplemented",
    "ExtensionTypeError",
    "RequiredPropertyMissing",
    "STACValidationError",
    "MediaType",
    "RelType",
    "StacIO",
    "STACObject",
    "STACObjectType",
    "Link",
    "HIERARCHICAL_LINKS",
    "Catalog",
    "CatalogType",
    "Collection",
    "Extent",
    "SpatialExtent",
    "TemporalExtent",
    "Summaries",
    "CommonMetadata",
    "RangeSummary",
    "Item",
    "Asset",
    "ItemCollection",
    "Provider",
    "ProviderRole",
    "read_file",
    "read_dict",
    "write_file",
    "get_stac_version",
    "set_stac_version",
]

from .errors import (
    STACError,
    STACTypeError,
    DuplicateObjectKeyError,
    ExtensionAlreadyExistsError,
    ExtensionNotImplemented,
    ExtensionTypeError,
    RequiredPropertyMissing,
    STACValidationError,
)

from typing import Any, Dict, Optional
from .version import (
    __version__,
    get_stac_version,
    set_stac_version,
)
from .media_type import MediaType
from .rel_type import RelType
from .stac_io import StacIO
from .stac_object import STACObject, STACObjectType
from .link import Link, HIERARCHICAL_LINKS
from .catalog import Catalog, CatalogType
from .collection import (
    Collection,
    Extent,
    SpatialExtent,
    TemporalExtent,
)
from .common_metadata import CommonMetadata
from .summaries import RangeSummary, Summaries
from .asset import Asset
from .item import Item
from .item_collection import ItemCollection
from .provider import ProviderRole, Provider
from . import validation

from .extensions import datacube
from .extensions import eo
from .extensions import file
from .extensions import item_assets
from .extensions import label
from .extensions import pointcloud
from .extensions import projection
from .extensions import sar
from .extensions import sat
from .extensions import scientific
from .extensions import table
from .extensions import timestamps
from .extensions import version
from .extensions import view

EXTENSION_HOOKS = extensions.hooks.RegisteredExtensionHooks(
    [
        datacube.DATACUBE_EXTENSION_HOOKS,
        eo.EO_EXTENSION_HOOKS,
        file.FILE_EXTENSION_HOOKS,
        item_assets.ITEM_ASSETS_EXTENSION_HOOKS,
        label.LABEL_EXTENSION_HOOKS,
        pointcloud.POINTCLOUD_EXTENSION_HOOKS,
        projection.PROJECTION_EXTENSION_HOOKS,
        sar.SAR_EXTENSION_HOOKS,
        sat.SAT_EXTENSION_HOOKS,
        scientific.SCIENTIFIC_EXTENSION_HOOKS,
        table.TABLE_EXTENSION_HOOKS,
        timestamps.TIMESTAMPS_EXTENSION_HOOKS,
        version.VERSION_EXTENSION_HOOKS,
        view.VIEW_EXTENSION_HOOKS,
    ]
)


def read_file(href: str, stac_io: Optional[StacIO] = None) -> STACObject:
    """Reads a STAC object from a file.

    This method will return either a Catalog, a Collection, or an Item based on what
    the file contains.

    This is a convenience method for :meth:`StacIO.read_stac_object
    <pystac.StacIO.read_stac_object>`

    Args:
        href : The HREF to read the object from.
        stac_io: Optional :class:`~StacIO` instance to use for I/O operations. If not
            provided, will use :meth:`StacIO.default` to create an instance.

    Returns:
        The specific STACObject implementation class that is represented
        by the JSON read from the file located at HREF.

    Raises:
        STACTypeError : If the file at ``href`` does not represent a valid
            :class:`~pystac.STACObject`. Note that an :class:`~pystac.ItemCollection`
            is not a :class:`~pystac.STACObject` and must be read using
            :meth:`ItemCollection.from_file <pystac.ItemCollection.from_file>`
    """
    if stac_io is None:
        stac_io = StacIO.default()
    return stac_io.read_stac_object(href)


def write_file(
    obj: STACObject,
    include_self_link: bool = True,
    dest_href: Optional[str] = None,
    stac_io: Optional[StacIO] = None,
) -> None:
    """Writes a STACObject to a file.

    This will write only the Catalog, Collection or Item ``obj``. It will not attempt
    to write any other objects that are linked to ``obj``; if you'd like functionality
    to save off catalogs recursively see :meth:`Catalog.save <pystac.Catalog.save>`.

    This method will write the JSON of the object to the object's assigned "self" link
    or to the dest_href if provided. To set the self link, see
    :meth:`STACObject.set_self_href <pystac.STACObject.set_self_href>`.

    Convenience method for :meth:`STACObject.from_file <pystac.STACObject.from_file>`

    Args:
        obj : The STACObject to save.
        include_self_link : If ``True``, include the ``"self"`` link with this object.
            Otherwise, leave out the self link.
        dest_href : Optional HREF to save the file to. If ``None``, the object will be
            saved to the object's ``"self"`` href.
        stac_io: Optional :class:`~StacIO` instance to use for I/O operations. If not
            provided, will use :meth:`StacIO.default` to create an instance.
    """
    if stac_io is None:
        stac_io = StacIO.default()
    obj.save_object(
        include_self_link=include_self_link, dest_href=dest_href, stac_io=stac_io
    )


def read_dict(
    d: Dict[str, Any],
    href: Optional[str] = None,
    root: Optional[Catalog] = None,
    stac_io: Optional[StacIO] = None,
) -> STACObject:
    """Reads a :class:`~STACObject` or :class:`~ItemCollection` from a JSON-like dict
    representing a serialized STAC object.

    This method will return either a :class:`~Catalog`, :class:`~Collection`,
    or :class`~Item` based on the contents of the dict.

    This is a convenience method for either
    :meth:`StacIO.stac_object_from_dict <pystac.StacIO.stac_object_from_dict>`.

    Args:
        d : The dict to parse.
        href : Optional href that is the file location of the object being
            parsed.
        root : Optional root of the catalog for this object.
            If provided, the root's resolved object cache can be used to search for
            previously resolved instances of the STAC object.
        stac_io: Optional :class:`~StacIO` instance to use for reading. If ``None``,
            the default instance will be used.

    Raises:
        STACTypeError : If the ``d`` dictionary does not represent a valid
            :class:`~pystac.STACObject`. Note that an :class:`~pystac.ItemCollection`
            is not a :class:`~pystac.STACObject` and must be read using
            :meth:`ItemCollection.from_dict <pystac.ItemCollection.from_dict>`
    """
    if stac_io is None:
        stac_io = StacIO.default()
    return stac_io.stac_object_from_dict(d, href, root)
