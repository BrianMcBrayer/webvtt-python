"""Tests for WebVTT data models."""

import pytest

from webvtt_python.models import (
    LineAlignment,
    PositionAlignment,
    TextAlignment,
    WebVTTCue,
    WebVTTRegion,
    WritingDirection,
)


class TestWebVTTCue:
    """Tests for WebVTTCue model."""

    def test_cue_validation(self):
        """Test validation of cue settings."""
        # Valid cue
        cue = WebVTTCue(
            start_time=0,
            end_time=1,
            text="Test",
            position=50,
            size=80,
        )
        assert cue.text == "Test"
        assert cue.position == 50
        assert cue.size == 80

        # Invalid timing
        with pytest.raises(ValueError):
            WebVTTCue(start_time=1, end_time=0, text="Test")

        # Invalid position
        with pytest.raises(ValueError):
            WebVTTCue(start_time=0, end_time=1, text="Test", position=101)

        # Invalid size
        with pytest.raises(ValueError):
            WebVTTCue(start_time=0, end_time=1, text="Test", size=-1)

    def test_cue_string_representation(self):
        """Test string representation of cues."""
        cue = WebVTTCue(
            identifier="1",
            start_time=61.5,  # 00:01:01.500
            end_time=65.2,  # 00:01:05.200
            text="Test cue",
            position=50,
            size=80,
            text_alignment=TextAlignment.START,
        )
        expected = "1\n00:01:01.500 --> 00:01:05.200 position:50% size:80% align:start\nTest cue"
        assert str(cue) == expected

    def test_cue_settings_formatting(self):
        """Test formatting of cue settings."""
        cue = WebVTTCue(
            start_time=0,
            end_time=1,
            text="Test",
            writing_direction=WritingDirection.VERTICAL_RL,
            line=5,
            position=50,
            size=80,
            text_alignment=TextAlignment.START,
        )
        settings = cue._format_settings()
        assert "vertical:rl" in settings
        assert "line:5" in settings
        assert "position:50%" in settings
        assert "size:80%" in settings
        assert "align:start" in settings


class TestWebVTTRegion:
    """Tests for WebVTTRegion model."""

    def test_region_defaults(self):
        """Test default values for region settings."""
        region = WebVTTRegion(id="test")
        assert region.id == "test"
        assert region.width == 100
        assert region.lines == 3
        assert region.region_anchor == (0, 100)
        assert region.viewport_anchor == (0, 100)
        assert region.scroll == "none"

    def test_region_custom_settings(self):
        """Test custom region settings."""
        region = WebVTTRegion(
            id="custom",
            width=40,
            lines=2,
            region_anchor=(10, 90),
            viewport_anchor=(20, 80),
            scroll="up",
        )
        assert region.id == "custom"
        assert region.width == 40
        assert region.lines == 2
        assert region.region_anchor == (10, 90)
        assert region.viewport_anchor == (20, 80)
        assert region.scroll == "up"


class TestEnums:
    """Tests for WebVTT enumeration types."""

    def test_text_alignment(self):
        """Test TextAlignment enum values."""
        assert TextAlignment.START.value == "start"
        assert TextAlignment.CENTER.value == "center"
        assert TextAlignment.END.value == "end"
        assert TextAlignment.LEFT.value == "left"
        assert TextAlignment.RIGHT.value == "right"

    def test_line_alignment(self):
        """Test LineAlignment enum values."""
        assert LineAlignment.START.value == "start"
        assert LineAlignment.CENTER.value == "center"
        assert LineAlignment.END.value == "end"

    def test_position_alignment(self):
        """Test PositionAlignment enum values."""
        assert PositionAlignment.LINE_LEFT.value == "line-left"
        assert PositionAlignment.CENTER.value == "center"
        assert PositionAlignment.LINE_RIGHT.value == "line-right"

    def test_writing_direction(self):
        """Test WritingDirection enum values."""
        assert WritingDirection.HORIZONTAL.value == "horizontal"
        assert WritingDirection.VERTICAL_RL.value == "vertical-rl"
        assert WritingDirection.VERTICAL_LR.value == "vertical-lr"
