"""WebVTT parser implementation.

This module provides the core parsing functionality for WebVTT files,
following the W3C WebVTT specification.
"""

import re
from dataclasses import dataclass
from typing import Any, Dict, List, Optional, TextIO, Union

from .models import (
    TextAlignment,
    WebVTT,
    WebVTTCue,
    WebVTTRegion,
    WritingDirection,
)


@dataclass
class Block:
    """Represents a block of WebVTT content."""

    type: str
    content: List[str]


class WebVTTParser:
    """Parser for WebVTT files."""

    # WebVTT timestamp format: hours:minutes:seconds.milliseconds
    # Hours: 00-99
    # Minutes: 00-59
    # Seconds: 00-59
    # Milliseconds: 000-999
    TIMESTAMP_PATTERN = re.compile(
        r"^(?P<hours>[0-9]{2}):(?P<minutes>[0-5][0-9]):(?P<seconds>[0-5][0-9])\.(?P<milliseconds>[0-9]{3})$"
    )

    # Cue timing line pattern
    TIMING_LINE_PATTERN = re.compile(
        r"^(?P<start>[0-9]{2}:[0-5][0-9]:[0-5][0-9]\.[0-9]{3})"
        r" --> "
        r"(?P<end>[0-9]{2}:[0-5][0-9]:[0-5][0-9]\.[0-9]{3})"
        r"(?P<settings>.*?)$"
    )

    def __init__(self, strict: bool = True):
        """Initialize the parser.

        Args:
            strict: If True, raise errors for invalid content. If False, try to recover.
        """
        self.strict = strict

    def parse(self, content: Union[str, TextIO]) -> WebVTT:
        """Parse WebVTT content from a string or file-like object."""
        # Convert input to lines
        if isinstance(content, str):
            lines = content.splitlines()
        else:
            lines = [line.rstrip() for line in content]

        # Validate header
        if not lines or not lines[0].strip().endswith("WEBVTT"):
            if self.strict:
                raise ValueError("Missing WEBVTT header")
            return WebVTT()

        # Split into blocks
        blocks = self._split_blocks(lines[1:])  # Skip WEBVTT line

        # Parse blocks
        webvtt = WebVTT()

        for block in blocks:
            if block.type == "header":
                # Only include actual header comments (before the first non-header block)
                if any(b.type != "header" for b in blocks[: blocks.index(block)]):
                    continue
                webvtt.header_comments.extend(block.content)
            elif block.type == "style":
                webvtt.styles.append("\n".join(block.content))
            elif block.type == "region":
                region = self._parse_region(block.content)
                if region:
                    webvtt.regions.append(region)
            elif block.type == "cue":
                cue = self._parse_cue(block.content)
                if cue:
                    webvtt.cues.append(cue)
            # NOTE blocks are ignored

        return webvtt

    def _split_blocks(self, lines: List[str]) -> List[Block]:
        """Split lines into blocks based on empty lines and block type markers."""
        blocks = []
        current_block = []
        current_type = "header"

        for line in lines:
            line = line.rstrip()

            # Empty line marks end of block
            if not line:
                if current_block:
                    blocks.append(Block(current_type, current_block))
                    current_block = []
                    current_type = "header"  # Reset to header type after empty line
                continue

            # Detect block type at start of block
            if not current_block:
                if line == "STYLE":
                    current_type = "style"
                    continue
                elif line == "REGION":
                    current_type = "region"
                    continue
                elif line == "NOTE":
                    current_type = "note"
                    continue
                elif "-->" in line:
                    current_type = "cue"
                    current_block.append(line)
                    continue

            # Start a new cue block if we see a timing line and we're not in a cue block
            if "-->" in line and current_type != "cue":
                if current_block:
                    blocks.append(Block(current_type, current_block))
                current_block = []
                current_type = "cue"

            current_block.append(line)

        # Add final block
        if current_block:
            blocks.append(Block(current_type, current_block))

        return blocks

    def _validate_timestamp(self, timestamp: str) -> bool:
        """Validate a timestamp string against the WebVTT format."""
        if timestamp is None:
            return False

        # First validate the format using regex
        if not self.TIMESTAMP_PATTERN.match(timestamp.strip()):
            return False

        # Additional validation of numeric ranges
        match = self.TIMESTAMP_PATTERN.match(timestamp.strip())
        hours = int(match.group("hours"))
        minutes = int(match.group("minutes"))
        seconds = int(match.group("seconds"))
        milliseconds = int(match.group("milliseconds"))

        return (
            0 <= hours <= 99
            and 0 <= minutes <= 59
            and 0 <= seconds <= 59
            and 0 <= milliseconds <= 999
        )

    def _parse_timestamp(self, timestamp: str) -> float:
        """Convert a timestamp string to seconds."""
        if not self._validate_timestamp(timestamp):
            if self.strict:
                raise ValueError(f"Invalid timestamp format: {timestamp}")
            return 0.0

        # Parse using manual calculation to support hours > 23
        match = self.TIMESTAMP_PATTERN.match(timestamp.strip())
        hours = int(match.group("hours"))
        minutes = int(match.group("minutes"))
        seconds = int(match.group("seconds"))
        milliseconds = int(match.group("milliseconds"))

        return hours * 3600 + minutes * 60 + seconds + milliseconds / 1000

    def _parse_cue(self, lines: List[str]) -> Optional[WebVTTCue]:
        """Parse a WebVTT cue block."""
        if not lines:
            return None

        # Find timing line
        timing_line = None
        timing_line_index = -1
        identifier = None

        for i, line in enumerate(lines):
            if "-->" in line:
                timing_line = line
                timing_line_index = i
                if i > 0:
                    identifier = "\n".join(lines[:i])
                break

        if not timing_line:
            if self.strict:
                raise ValueError("No timing information found in cue")
            return None

        # Parse timing line
        match = self.TIMING_LINE_PATTERN.match(timing_line)
        if not match:
            if self.strict:
                raise ValueError(f"Invalid timing line format: {timing_line}")
            return None

        try:
            start_time = self._parse_timestamp(match.group("start"))
            end_time = self._parse_timestamp(match.group("end"))
            settings = self._parse_cue_settings(match.group("settings"))

            # Get cue text
            text_lines = lines[timing_line_index + 1 :]
            text = "\n".join(text_lines) if text_lines else ""

            return WebVTTCue(
                start_time=start_time,
                end_time=end_time,
                text=text,
                identifier=identifier,
                **settings,
            )
        except ValueError as e:
            if self.strict:
                raise ValueError(f"Invalid cue: {str(e)}")
            return None

    def _parse_cue_settings(self, settings_str: str) -> Dict[str, Any]:
        """Parse WebVTT cue settings."""
        settings = {}
        if not settings_str:
            return settings

        for setting in settings_str.strip().split():
            if ":" not in setting:
                continue
            name, value = setting.split(":", 1)

            if name == "region":
                settings["region"] = value
            elif name == "vertical":
                settings["writing_direction"] = WritingDirection(f"vertical-{value}")
            elif name == "line":
                if value.endswith("%"):
                    settings["line"] = float(value[:-1])
                    settings["snap_to_lines"] = False
                else:
                    settings["line"] = float(value)
                    settings["snap_to_lines"] = True
            elif name == "position":
                if value.endswith("%"):
                    settings["position"] = float(value[:-1])
            elif name == "size":
                if value.endswith("%"):
                    settings["size"] = float(value[:-1])
            elif name == "align":
                settings["text_alignment"] = TextAlignment(value)

        return settings

    def _parse_region_settings(self, settings: List[str]) -> WebVTTRegion:
        """Parse region settings into a WebVTTRegion object."""
        region = WebVTTRegion()

        for setting in settings:
            if not setting:
                continue

            try:
                key, value = setting.split(":", 1)
            except ValueError:
                raise ValueError(f"Invalid region setting format: {setting}")

            key = key.strip().lower()
            value = value.strip()

            if key == "id":
                region.id = value
            elif key == "width":
                try:
                    width = float(value.rstrip("%"))
                    if width < 0 or width > 100:
                        raise ValueError
                    region.width = width
                except ValueError:
                    raise ValueError(f"Invalid region width: {value}")
            elif key == "lines":
                try:
                    lines = int(value)
                    if lines < 1:
                        raise ValueError
                    region.lines = lines
                except ValueError:
                    raise ValueError(f"Invalid region lines: {value}")
            elif key == "regionanchor":
                try:
                    x, y = value.split(",")
                    x = float(x.rstrip("%"))
                    y = float(y.rstrip("%"))
                    if x < 0 or x > 100 or y < 0 or y > 100:
                        raise ValueError
                    region.region_anchor = (x, y)
                except (ValueError, IndexError):
                    raise ValueError(f"Invalid region anchor: {value}")
            elif key == "viewportanchor":
                try:
                    x, y = value.split(",")
                    x = float(x.rstrip("%"))
                    y = float(y.rstrip("%"))
                    if x < 0 or x > 100 or y < 0 or y > 100:
                        raise ValueError
                    region.viewport_anchor = (x, y)
                except (ValueError, IndexError):
                    raise ValueError(f"Invalid viewport anchor: {value}")
            elif key == "scroll":
                if value not in ("", "up"):
                    raise ValueError(f"Invalid scroll value: {value}")
                region.scroll = value or "none"
            else:
                raise ValueError(f"Unknown region setting: {key}")

        return region

    def _parse_region(self, lines: List[str]) -> Optional[WebVTTRegion]:
        """Parse a WebVTT region block."""
        if not lines:
            return None

        try:
            region = self._parse_region_settings(lines)
            return region
        except ValueError as e:
            if self.strict:
                raise ValueError(f"Invalid region: {str(e)}")
            return None

    @staticmethod
    def _parse_anchor(anchor_str: str) -> tuple:
        """Parse a region anchor string into x,y coordinates."""
        try:
            x, y = anchor_str.split(",")
            return (float(x.strip().rstrip("%")), float(y.strip().rstrip("%")))
        except (ValueError, AttributeError):
            return (0, 100)
