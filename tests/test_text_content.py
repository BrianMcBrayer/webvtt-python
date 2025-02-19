"""Tests for WebVTT text content and markup parsing."""

import pytest

from webvtt_python import WebVTTParser


@pytest.fixture
def parser():
    """Create a WebVTT parser instance."""
    return WebVTTParser()


class TestBasicText:
    """Tests for basic text content parsing."""

    def test_single_line_cue(self, parser):
        """Test parsing of single-line cues."""
        content = """WEBVTT

00:00:01.000 --> 00:00:02.000
Simple text"""
        webvtt = parser.parse(content)
        assert len(webvtt.cues) == 1
        assert webvtt.cues[0].text == "Simple text"

    def test_multi_line_cue(self, parser):
        """Test parsing of multi-line cues."""
        content = """WEBVTT

00:00:01.000 --> 00:00:02.000
First line
Second line
Third line"""
        webvtt = parser.parse(content)
        assert len(webvtt.cues) == 1
        assert webvtt.cues[0].text == "First line\nSecond line\nThird line"

    def test_empty_cue(self, parser):
        """Test parsing of empty cues."""
        content = """WEBVTT

00:00:01.000 --> 00:00:02.000

00:00:02.000 --> 00:00:03.000
Text"""
        webvtt = parser.parse(content)
        assert len(webvtt.cues) == 2
        assert webvtt.cues[0].text == ""
        assert webvtt.cues[1].text == "Text"

    def test_whitespace_handling(self, parser):
        """Test handling of various whitespace characters."""
        content = """WEBVTT

00:00:01.000 --> 00:00:02.000
  Leading spaces
Trailing spaces
  Both sides
\tTab character
Multiple     spaces"""
        webvtt = parser.parse(content)
        assert len(webvtt.cues) == 1
        # According to WebVTT spec, trailing whitespace should be trimmed
        expected = (
            "  Leading spaces\nTrailing spaces\n  Both sides\n\tTab character\nMultiple     spaces"
        )
        assert webvtt.cues[0].text == expected

    def test_unicode_characters(self, parser):
        """Test parsing of Unicode characters."""
        content = """WEBVTT

00:00:01.000 --> 00:00:02.000
Hello 世界
Café au lait
🌟 Stars ✨"""
        webvtt = parser.parse(content)
        assert len(webvtt.cues) == 1
        assert webvtt.cues[0].text == "Hello 世界\nCafé au lait\n🌟 Stars ✨"


class TestMarkup:
    """Tests for WebVTT markup parsing."""

    def test_voice_spans(self, parser):
        """Test parsing of voice spans."""
        content = """WEBVTT

00:00:01.000 --> 00:00:02.000
<v John>Hello, how are you?</v>
<v Mary>I'm fine, thank you!</v>"""
        webvtt = parser.parse(content)
        assert len(webvtt.cues) == 1
        assert "<v John>" in webvtt.cues[0].text
        assert "<v Mary>" in webvtt.cues[0].text

    def test_ruby_text(self, parser):
        """Test parsing of ruby text."""
        content = """WEBVTT

00:00:01.000 --> 00:00:02.000
<ruby>漢字<rt>かんじ</rt></ruby>"""
        webvtt = parser.parse(content)
        assert len(webvtt.cues) == 1
        assert webvtt.cues[0].text == "<ruby>漢字<rt>かんじ</rt></ruby>"

    def test_class_annotations(self, parser):
        """Test parsing of class annotations."""
        content = """WEBVTT

00:00:01.000 --> 00:00:02.000
<c.highlight>Important text</c>
<c.italic.blue>Styled text</c>"""
        webvtt = parser.parse(content)
        assert len(webvtt.cues) == 1
        assert "<c.highlight>" in webvtt.cues[0].text
        assert "<c.italic.blue>" in webvtt.cues[0].text

    def test_nested_markup(self, parser):
        """Test parsing of nested markup."""
        content = """WEBVTT

00:00:01.000 --> 00:00:02.000
<v John><c.angry>I am very upset!</c></v>
<v Mary><c.calm>Please <i>calm</i> down.</c></v>"""
        webvtt = parser.parse(content)
        assert len(webvtt.cues) == 1
        text = webvtt.cues[0].text
        assert "<v John>" in text
        assert "<c.angry>" in text
        assert "<v Mary>" in text
        assert "<c.calm>" in text
        assert "<i>calm</i>" in text

    def test_invalid_markup_recovery(self, parser):
        """Test recovery from invalid markup."""
        content = """WEBVTT

00:00:01.000 --> 00:00:02.000
<v>Missing speaker
<c.invalid>Unclosed tag
<unknown>Invalid tag</unknown>"""
        webvtt = parser.parse(content)
        assert len(webvtt.cues) == 1
        # The parser should preserve invalid markup as-is
        assert "<v>Missing speaker" in webvtt.cues[0].text
        assert "<c.invalid>Unclosed tag" in webvtt.cues[0].text
        assert "<unknown>Invalid tag</unknown>" in webvtt.cues[0].text


class TestEscapeSequences:
    """Tests for WebVTT escape sequence handling."""

    def test_escape_sequences(self, parser):
        """Test parsing of escape sequences."""
        content = """WEBVTT

00:00:01.000 --> 00:00:02.000
&amp; ampersand
&lt; less than
&gt; greater than
&lrm; left-to-right mark
&rlm; right-to-left mark"""
        webvtt = parser.parse(content)
        assert len(webvtt.cues) == 1
        text = webvtt.cues[0].text
        assert "&amp;" in text
        assert "&lt;" in text
        assert "&gt;" in text
        assert "&lrm;" in text
        assert "&rlm;" in text
