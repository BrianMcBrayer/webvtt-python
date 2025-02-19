"""Tests for WebVTT style block parsing."""

import pytest

from webvtt_python import WebVTTParser


@pytest.fixture
def parser():
    """Create a WebVTT parser instance."""
    return WebVTTParser()


class TestStyleParsing:
    """Tests for WebVTT style block parsing."""

    def test_basic_style_block(self, parser):
        """Test parsing of a basic style block."""
        content = """WEBVTT

STYLE
::cue {
    color: red;
    background: black;
}

00:00:01.000 --> 00:00:02.000
Test"""
        webvtt = parser.parse(content)
        assert len(webvtt.styles) == 1
        assert "color: red" in webvtt.styles[0]
        assert "background: black" in webvtt.styles[0]

    def test_multiple_style_blocks(self, parser):
        """Test parsing of multiple style blocks."""
        content = """WEBVTT

STYLE
::cue {
    color: red;
}

STYLE
::cue(b) {
    font-weight: bold;
}

00:00:01.000 --> 00:00:02.000
Test"""
        webvtt = parser.parse(content)
        assert len(webvtt.styles) == 2
        assert "color: red" in webvtt.styles[0]
        assert "font-weight: bold" in webvtt.styles[1]

    def test_class_based_styling(self, parser):
        """Test parsing of class-based style rules."""
        content = """WEBVTT

STYLE
::cue(.red) {
    color: red;
}

STYLE
::cue(.bold) {
    font-weight: bold;
}

00:00:01.000 --> 00:00:02.000
<c.red>Red text</c>"""
        webvtt = parser.parse(content)
        assert len(webvtt.styles) == 2
        assert "::cue(.red)" in webvtt.styles[0]
        assert "::cue(.bold)" in webvtt.styles[1]

    def test_voice_based_styling(self, parser):
        """Test parsing of voice-based style rules."""
        content = """WEBVTT

STYLE
::cue(v[voice="John"]) {
    color: blue;
}

00:00:01.000 --> 00:00:02.000
<v John>Hello</v>"""
        webvtt = parser.parse(content)
        assert len(webvtt.styles) == 1
        assert 'v[voice="John"]' in webvtt.styles[0]
        assert "color: blue" in webvtt.styles[0]

    def test_invalid_css_syntax(self, parser):
        """Test handling of invalid CSS syntax."""
        content = """WEBVTT

STYLE
::cue {
    invalid-property: value;
    color: invalid-color;
    background: ;
}

00:00:01.000 --> 00:00:02.000
Test"""
        webvtt = parser.parse(content)
        # Parser should preserve invalid CSS as-is
        assert len(webvtt.styles) == 1
        assert "invalid-property: value" in webvtt.styles[0]

    def test_complex_selectors(self, parser):
        """Test parsing of complex CSS selectors."""
        content = """WEBVTT

STYLE
::cue(b.red) {
    color: red;
}

STYLE
::cue(i[voice="John"].blue) {
    color: blue;
}

00:00:01.000 --> 00:00:02.000
<v John><i class="blue">Hello</i></v>"""
        webvtt = parser.parse(content)
        assert len(webvtt.styles) == 2
        assert "::cue(b.red)" in webvtt.styles[0]
        assert 'i[voice="John"].blue' in webvtt.styles[1]


class TestStylePerformance:
    """Tests for style parsing performance."""

    def test_large_style_block(self, parser):
        """Test parsing of a large style block."""
        # Create a style block with 1000 rules
        rules = []
        for i in range(1000):
            rules.append(f"""::cue(.class{i}) {{
    color: rgb({i % 255}, {(i + 85) % 255}, {(i + 170) % 255});
    background: black;
    font-size: {(i % 20) + 10}px;
}}""")

        content = "WEBVTT\n\nSTYLE\n" + "\n".join(rules) + "\n\n00:00:01.000 --> 00:00:02.000\nTest"

        import time

        start_time = time.time()
        webvtt = parser.parse(content)
        parse_time = time.time() - start_time

        assert len(webvtt.styles) == 1
        assert parse_time < 1.0  # Should parse in under 1 second
