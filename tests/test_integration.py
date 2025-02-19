"""Integration tests for WebVTT parser."""

from io import StringIO

import pytest

from webvtt_python import WebVTT, WritingDirection


class TestFileIO:
    """Tests for file I/O operations."""

    def test_string_parsing(self, parser, sample_webvtt):
        """Test parsing from string input."""
        webvtt = parser.parse(sample_webvtt)
        assert isinstance(webvtt, WebVTT)
        assert len(webvtt.cues) == 2

    def test_file_parsing(self, parser, sample_webvtt, tmp_path):
        """Test parsing from file input."""
        # Write sample to temporary file
        vtt_file = tmp_path / "test.vtt"
        vtt_file.write_text(sample_webvtt)

        # Parse from file object
        with open(vtt_file, "r") as f:
            webvtt = parser.parse(f)
            assert isinstance(webvtt, WebVTT)
            assert len(webvtt.cues) == 2

    def test_stream_parsing(self, parser, sample_webvtt):
        """Test parsing from stream input."""
        stream = StringIO(sample_webvtt)
        webvtt = parser.parse(stream)
        assert isinstance(webvtt, WebVTT)
        assert len(webvtt.cues) == 2


class TestCompleteWorkflow:
    """End-to-end tests for WebVTT parsing workflow."""

    def test_complete_parse_and_format(self, parser):
        """Test parsing and reformatting of a complete WebVTT file."""
        original = """WEBVTT
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

1
00:00:02.500 --> 00:00:05.000 line:75% position:50% align:center
<v Fred>Hi, I'm Fred!</v>

2
00:00:07.800 --> 00:00:11.000 vertical:rl region:fred
That's all for now!"""

        # Parse the original
        webvtt = parser.parse(original)

        # Convert back to string
        result = str(webvtt)

        # Parse the result again
        reparsed = parser.parse(result)

        # Verify the structure is preserved
        assert len(reparsed.regions) == len(webvtt.regions)
        assert len(reparsed.styles) == len(webvtt.styles)
        assert len(reparsed.cues) == len(webvtt.cues)

        # Verify cue content is preserved
        assert reparsed.cues[0].text == "<v Fred>Hi, I'm Fred!</v>"
        assert reparsed.cues[1].text == "That's all for now!"

        # Verify cue settings are preserved
        assert reparsed.cues[0].line == 75
        assert reparsed.cues[0].position == 50
        assert reparsed.cues[1].writing_direction == WritingDirection.VERTICAL_RL
        assert reparsed.cues[1].region == "fred"

    def test_error_propagation(self, parser):
        """Test that errors are properly propagated through the parsing chain."""
        invalid_content = """WEBVTT

00:00:01.000 --> invalid
Test

STYLE
::invalid-css {
    color: invalid;
}

00:00:02.000 --> 00:00:03.000 invalid:setting
Another test"""

        with pytest.raises(ValueError) as exc_info:
            parser.parse(invalid_content)
        assert "Invalid" in str(exc_info.value)
