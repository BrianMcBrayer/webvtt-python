"""WebVTT data models.

This module defines the core data structures for representing WebVTT content,
including cues, regions, and their associated settings.
"""

from dataclasses import dataclass, field
from enum import Enum
from typing import Dict, List, Optional, Tuple


class TextAlignment(Enum):
    """Text alignment options for WebVTT cues."""

    START = "start"
    CENTER = "center"
    END = "end"
    LEFT = "left"
    RIGHT = "right"


class LineAlignment(Enum):
    """Line alignment options for WebVTT cues."""

    START = "start"
    CENTER = "center"
    END = "end"


class PositionAlignment(Enum):
    """Position alignment options for WebVTT cues."""

    LINE_LEFT = "line-left"
    CENTER = "center"
    LINE_RIGHT = "line-right"
    AUTO = "auto"


class WritingDirection(Enum):
    """Writing direction options for WebVTT cues."""

    HORIZONTAL = "horizontal"
    VERTICAL_RL = "vertical-rl"
    VERTICAL_LR = "vertical-lr"


@dataclass
class WebVTTRegion:
    """Represents a WebVTT region for positioning cues."""

    id: str = ""
    width: float = 100.0
    lines: int = 3
    region_anchor: Tuple[float, float] = (0, 100)
    viewport_anchor: Tuple[float, float] = (0, 100)
    scroll: str = "none"


@dataclass
class WebVTTCue:
    """Represents a WebVTT cue with timing and display information."""

    start_time: float
    end_time: float
    text: str
    identifier: Optional[str] = None

    # Positioning and formatting settings
    region: Optional[str] = None
    writing_direction: Optional[WritingDirection] = None
    line: Optional[float] = None
    line_alignment: LineAlignment = LineAlignment.START
    position: Optional[float] = None
    position_alignment: PositionAlignment = PositionAlignment.CENTER
    size: float = 100.0
    text_alignment: TextAlignment = TextAlignment.CENTER
    snap_to_lines: bool = True

    # Internal state
    styles: Dict = field(default_factory=dict)
    nodes: List = field(default_factory=list)

    def __post_init__(self):
        """Validate cue settings after initialization."""
        if self.start_time < 0 or self.end_time < 0:
            raise ValueError("Cue times cannot be negative")
        if self.start_time >= self.end_time:
            raise ValueError("Cue end time must be greater than start time")
        if self.position is not None and (self.position < 0 or self.position > 100):
            raise ValueError("Position must be between 0 and 100")
        if self.size < 0 or self.size > 100:
            raise ValueError("Size must be between 0 and 100")

    def _format_timestamp(self, seconds: float) -> str:
        """Format a timestamp in seconds to WebVTT format."""
        hours = int(seconds // 3600)
        minutes = int((seconds % 3600) // 60)
        seconds = seconds % 60
        return f"{hours:02d}:{minutes:02d}:{seconds:06.3f}"

    def _format_settings(self) -> str:
        """Format cue settings as a string."""
        settings = []
        if self.region:
            settings.append(f"region:{self.region}")
        if self.writing_direction:
            direction = self.writing_direction.value
            if direction.startswith("vertical-"):
                settings.append(f"vertical:{direction.split('-')[1]}")
        if self.line is not None:
            settings.append(f"line:{self.line}{'%' if not self.snap_to_lines else ''}")
        if self.position is not None:
            settings.append(f"position:{self.position}%")
        if self.size != 100:
            settings.append(f"size:{self.size}%")
        if self.text_alignment != TextAlignment.CENTER:
            settings.append(f"align:{self.text_alignment.value}")
        return " ".join(settings)

    def __str__(self) -> str:
        """Return string representation of the cue."""
        parts = []
        if self.identifier:
            parts.append(self.identifier)
        timing = (
            f"{self._format_timestamp(self.start_time)} --> {self._format_timestamp(self.end_time)}"
        )
        settings = self._format_settings()
        if settings:
            timing += f" {settings}"
        parts.append(timing)
        parts.append(self.text)
        return "\n".join(parts)


@dataclass
class WebVTT:
    """Represents a parsed WebVTT file."""

    cues: List[WebVTTCue] = field(default_factory=list)
    regions: List[WebVTTRegion] = field(default_factory=list)
    styles: List[str] = field(default_factory=list)
    header_comments: List[str] = field(default_factory=list)

    def __str__(self) -> str:
        """Return string representation of the WebVTT file."""
        parts = ["WEBVTT"]

        # Add header comments
        if self.header_comments:
            parts.extend(self.header_comments)

        # Add regions
        for region in self.regions:
            parts.append("\nREGION")
            if region.id:
                parts.append(f"id:{region.id}")
            parts.append(f"width:{region.width}%")
            parts.append(f"lines:{region.lines}")
            if region.region_anchor != (0, 100):
                parts.append(f"regionanchor:{region.region_anchor[0]}%,{region.region_anchor[1]}%")
            if region.viewport_anchor != (0, 100):
                parts.append(
                    f"viewportanchor:{region.viewport_anchor[0]}%,{region.viewport_anchor[1]}%"
                )
            if region.scroll != "none":
                parts.append(f"scroll:{region.scroll}")

        # Add styles
        for style in self.styles:
            parts.append(f"\nSTYLE\n{style}")

        # Add cues
        for cue in self.cues:
            parts.append(f"\n{cue}")

        return "\n".join(parts)
