"""Test configuration and fixtures for WebVTT parser tests."""

from typing import List, Tuple

import pytest

from webvtt_python import WebVTTParser


@pytest.fixture
def parser():
    """Create a WebVTTParser instance in strict mode."""
    return WebVTTParser(strict=True)


@pytest.fixture
def lenient_parser():
    """Create a WebVTTParser instance in lenient mode."""
    return WebVTTParser(strict=False)


@pytest.fixture
def sample_webvtt() -> str:
    """Return a sample WebVTT file content with various features."""
    return """WEBVTT
Kind: captions
Language: en-US

REGION
id:fred
width:40%
lines:3
regionanchor:0%,100%
viewportanchor:10%,90%
scroll:up

STYLE
::cue {
    color: yellow;
    background: rgba(0,0,0,0.8);
}

NOTE This is a comment
with multiple lines

1
00:00:02.500 --> 00:00:05.000 line:75% position:50% align:center
<v Fred>Hi, I'm Fred!</v>

2
00:00:07.800 --> 00:00:11.000 vertical:rl region:fred
That's all for now!"""


@pytest.fixture
def sample_regions() -> List[Tuple[str, str]]:
    """Return a list of (region_id, region_content) tuples for testing."""
    return [
        (
            "simple",
            """id:simple
width:50%
lines:2""",
        ),
        (
            "complex",
            """id:complex
width:40%
lines:3
regionanchor:10%,90%
viewportanchor:20%,80%
scroll:up""",
        ),
    ]


@pytest.fixture
def sample_cues() -> List[Tuple[str, str, str]]:
    """Return a list of (id, timing, content) tuples for testing."""
    return [
        ("1", "00:00:01.000 --> 00:00:02.000", "Basic cue"),
        (
            "2",
            "00:00:02.500 --> 00:00:05.000 line:75% position:50% align:center",
            "<v Fred>Styled cue</v>",
        ),
        (
            "3",
            "00:01:02.000 --> 00:01:05.000 vertical:rl region:fred",
            "Region cue\nwith multiple\nlines",
        ),
    ]
