"""Tests for the WebVTT parser implementation."""

import pytest
from hypothesis import given
from hypothesis import strategies as st

from webvtt_python import WebVTT
from webvtt_python.models import (
    TextAlignment,
    WebVTTCue,
    WritingDirection,
)


class TestFileStructure:
    """Tests for WebVTT file structure parsing."""

    def test_valid_header(self, parser, sample_webvtt):
        """Test parsing of valid WebVTT header."""
        webvtt = parser.parse(sample_webvtt)
        assert isinstance(webvtt, WebVTT)
        assert len(webvtt.header_comments) == 2
        assert webvtt.header_comments[0] == "Kind: captions"
        assert webvtt.header_comments[1] == "Language: en-US"

    def test_missing_header(self, parser):
        """Test that parser rejects files without WEBVTT header."""
        with pytest.raises(ValueError, match="Missing WEBVTT header"):
            parser.parse("Invalid content\n00:00:01.000 --> 00:00:02.000\nTest")

    def test_bom_handling(self, parser):
        """Test parsing of WebVTT file with BOM."""
        content = "\ufeffWEBVTT\n\n00:00:01.000 --> 00:00:02.000\nTest"
        webvtt = parser.parse(content)
        assert len(webvtt.cues) == 1
        assert webvtt.cues[0].text == "Test"

    def test_block_types(self, parser, sample_webvtt):
        """Test parsing of different block types."""
        webvtt = parser.parse(sample_webvtt)
        assert len(webvtt.regions) == 1
        assert len(webvtt.styles) == 1
        assert len(webvtt.cues) == 2


class TestTimingParsing:
    """Tests for WebVTT timestamp parsing."""

    @pytest.mark.parametrize(
        "timestamp,expected_seconds",
        [
            ("00:00:01.000", 1.0),
            ("00:01:00.000", 60.0),
            ("01:00:00.000", 3600.0),
            ("12:34:56.789", 45296.789),
        ],
    )
    def test_timestamp_parsing(self, parser, timestamp, expected_seconds):
        """Test parsing of various timestamp formats."""
        content = f"WEBVTT\n\n{timestamp} --> {timestamp.split(':')[0]}:59:59.999\nTest"
        webvtt = parser.parse(content)
        assert webvtt.cues[0].start_time == expected_seconds

    def test_invalid_timestamp(self, parser):
        """Test handling of invalid timestamp format."""
        content = "WEBVTT\n\n0:0:1.000 --> 00:00:02.000\nTest"
        with pytest.raises(ValueError):
            parser.parse(content)

    def test_timestamp_ordering(self, parser):
        """Test that end time must be after start time."""
        content = "WEBVTT\n\n00:00:02.000 --> 00:00:01.000\nTest"
        with pytest.raises(ValueError, match="Cue end time must be greater than start time"):
            parser.parse(content)


class TestRegionParsing:
    """Tests for WebVTT region parsing."""

    def test_region_settings(self, parser):
        """Test parsing of region settings."""
        content = """WEBVTT

REGION
id:test
width:40%
lines:3
regionanchor:10%,90%
viewportanchor:20%,80%
scroll:up

00:00:01.000 --> 00:00:02.000 region:test
Test"""
        webvtt = parser.parse(content)
        region = webvtt.regions[0]
        assert region.id == "test"
        assert region.width == 40
        assert region.lines == 3
        assert region.region_anchor == (10, 90)
        assert region.viewport_anchor == (20, 80)
        assert region.scroll == "up"

    def test_invalid_region(self, parser):
        """Test handling of invalid region settings."""
        content = """WEBVTT

REGION
id:test
width:invalid
lines:3

00:00:01.000 --> 00:00:02.000
Test"""
        with pytest.raises(ValueError):
            parser.parse(content)


class TestCueSettings:
    """Tests for WebVTT cue settings parsing."""

    def test_cue_positioning(self, parser):
        """Test parsing of cue positioning settings."""
        content = """WEBVTT

00:00:01.000 --> 00:00:02.000 line:5 position:50% size:80% align:start
Test"""
        webvtt = parser.parse(content)
        cue = webvtt.cues[0]
        assert cue.line == 5
        assert cue.position == 50
        assert cue.size == 80
        assert cue.text_alignment == TextAlignment.START

    def test_writing_direction(self, parser):
        """Test parsing of writing direction settings."""
        content = """WEBVTT

00:00:01.000 --> 00:00:02.000 vertical:rl
Test"""
        webvtt = parser.parse(content)
        cue = webvtt.cues[0]
        assert cue.writing_direction == WritingDirection.VERTICAL_RL


class TestTextContent:
    """Tests for WebVTT text content parsing."""

    def test_multiline_cue(self, parser):
        """Test parsing of multi-line cues."""
        content = """WEBVTT

00:00:01.000 --> 00:00:02.000
First line
Second line
Third line"""
        webvtt = parser.parse(content)
        assert webvtt.cues[0].text == "First line\nSecond line\nThird line"

    def test_voice_markup(self, parser):
        """Test parsing of voice markup."""
        content = """WEBVTT

00:00:01.000 --> 00:00:02.000
<v Fred>Hello</v>"""
        webvtt = parser.parse(content)
        assert webvtt.cues[0].text == "<v Fred>Hello</v>"


class TestErrorHandling:
    """Tests for WebVTT parser error handling."""

    def test_strict_mode(self, parser):
        """Test that strict mode raises errors for invalid content."""
        content = """WEBVTT

00:00:01.000 --> invalid
Test"""
        with pytest.raises(ValueError):
            parser.parse(content)

    def test_lenient_mode(self, lenient_parser):
        """Test that lenient mode skips invalid content."""
        content = """WEBVTT

00:00:01.000 --> invalid
Test

00:00:02.000 --> 00:00:03.000
Valid cue"""
        webvtt = lenient_parser.parse(content)
        assert len(webvtt.cues) == 1
        assert webvtt.cues[0].text == "Valid cue"


class TestPropertyBasedTests:
    """Property-based tests using Hypothesis."""

    @given(st.floats(min_value=0, max_value=86400))
    def test_timestamp_roundtrip(self, seconds):
        """Test that timestamp conversion is reversible."""
        cue = WebVTTCue(start_time=seconds, end_time=seconds + 1, text="Test")
        assert abs(float(cue._format_timestamp(seconds).split(":")[-1]) - (seconds % 60)) < 0.001

    @given(st.text(min_size=1))
    def test_cue_text(self, text):
        """Test that any valid text can be used in cues."""
        cue = WebVTTCue(start_time=0, end_time=1, text=text)
        assert cue.text == text
