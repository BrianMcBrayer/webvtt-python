"""Python WebVTT API Implementation.

This package provides a parser and API for working with WebVTT (Web Video Text Tracks) files,
following the W3C WebVTT specification.
"""

from .models import (
    LineAlignment,
    PositionAlignment,
    TextAlignment,
    WebVTTCue,
    WebVTTRegion,
    WritingDirection,
)
from .parser import WebVTT, WebVTTParser

__version__ = "0.1.0"
__all__ = [
    "WebVTTParser",
    "WebVTT",
    "WebVTTCue",
    "WebVTTRegion",
    "TextAlignment",
    "LineAlignment",
    "PositionAlignment",
    "WritingDirection",
]
