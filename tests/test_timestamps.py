"""Tests for WebVTT timestamp parsing and validation."""

import pytest

from webvtt_python.parser import WebVTTParser


class TestTimestampParsing:
    """Test suite for timestamp parsing functionality."""

    @pytest.fixture
    def parser(self):
        return WebVTTParser(strict=True)

    def test_valid_timestamps(self, parser):
        """Test parsing of valid timestamp formats."""
        test_cases = [
            ("00:00:00.000", 0.0),
            ("01:23:45.678", 5025.678),
            ("99:59:59.999", 359999.999),
            ("00:00:01.500", 1.5),
            ("00:01:00.000", 60.0),
            ("01:00:00.000", 3600.0),
        ]

        for timestamp, expected in test_cases:
            assert parser._parse_timestamp(timestamp) == expected

    def test_invalid_timestamps(self, parser):
        """Test handling of invalid timestamp formats."""
        invalid_timestamps = [
            "00:60:00.000",  # Minutes > 59
            "00:00:60.000",  # Seconds > 59
            "00:00:00.1000",  # Milliseconds > 999
            "0:0:0.000",  # Missing leading zeros
            "00:00:00",  # Missing milliseconds
            "not a timestamp",
            "",
            None,
        ]

        for timestamp in invalid_timestamps:
            with pytest.raises(ValueError):
                parser._parse_timestamp(timestamp)

    def test_lenient_mode_timestamps(self):
        """Test timestamp handling in lenient mode."""
        parser = WebVTTParser(strict=False)

        # Invalid timestamps should return 0.0 in lenient mode
        assert parser._parse_timestamp("invalid") == 0.0
        assert parser._parse_timestamp("") == 0.0
        assert parser._parse_timestamp(None) == 0.0

    def test_edge_case_timestamps(self, parser):
        """Test edge cases in timestamp parsing."""
        # Maximum valid timestamp
        assert parser._parse_timestamp("99:59:59.999") == 359999.999

        # Minimum valid timestamp
        assert parser._parse_timestamp("00:00:00.000") == 0.0

        # Just below/above valid ranges
        with pytest.raises(ValueError):
            parser._parse_timestamp("100:00:00.000")
        with pytest.raises(ValueError):
            parser._parse_timestamp("00:00:00.1000")

    def test_timestamp_validation(self, parser):
        """Test timestamp validation logic."""
        assert parser._validate_timestamp("00:00:00.000") is True
        assert parser._validate_timestamp("invalid") is False
        assert parser._validate_timestamp("") is False
        assert parser._validate_timestamp(None) is False
