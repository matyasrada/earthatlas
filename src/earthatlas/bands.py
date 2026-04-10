"""Sentinel-2 band combinations for Earth Search STAC catalog."""

from types import SimpleNamespace

composites = SimpleNamespace(
    true_color=["red", "green", "blue"],
    false_color=["nir", "red", "green"],
    swir=["swir22", "nir", "red"],
    bathymetric=["coastal", "blue", "green"],
    ag=["swir16", "nir", "blue"],
)
