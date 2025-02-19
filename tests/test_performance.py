"""Performance and integration tests for WebVTT parser."""

import os
import tempfile
from concurrent.futures import ThreadPoolExecutor
from io import StringIO

import pytest

from webvtt_python import WebVTTParser


@pytest.fixture
def parser():
    """Create a WebVTT parser instance."""
    return WebVTTParser()


@pytest.fixture
def large_webvtt_file():
    """Create a temporary large WebVTT file."""
    with tempfile.NamedTemporaryFile(mode="w", delete=False, suffix=".vtt") as f:
        f.write("WEBVTT\n\n")
        # Create 1000 cues (reduced from 10000 to speed up tests)
        for i in range(1000):
            hours = i // 3600
            minutes = (i % 3600) // 60
            seconds = i % 60
            next_seconds = (i + 1) % 60
            next_minutes = ((i + 1) % 3600) // 60
            next_hours = (i + 1) // 3600

            f.write(
                f"{hours:02d}:{minutes:02d}:{seconds:02d}.000 --> "
                f"{next_hours:02d}:{next_minutes:02d}:{next_seconds:02d}.000\n"
            )
            f.write(f"Cue {i}\n\n")
    yield f.name
    os.unlink(f.name)


class TestPerformance:
    """Performance tests for WebVTT parser."""

    def test_large_file_memory(self, parser, large_webvtt_file):
        """Test memory usage with large files."""
        import os

        import psutil

        process = psutil.Process(os.getpid())
        initial_memory = process.memory_info().rss

        with open(large_webvtt_file, "r") as f:
            webvtt = parser.parse(f.read())

        final_memory = process.memory_info().rss
        memory_increase = (final_memory - initial_memory) / 1024 / 1024  # Convert to MB

        assert len(webvtt.cues) == 1000
        assert memory_increase < 50  # Should use less than 50MB additional memory

    def test_parse_time_scaling(self, parser):
        """Test parse time scaling with file size."""
        import time

        # Test with different file sizes
        sizes = [10, 100, 1000]
        times = []

        for size in sizes:
            content = "WEBVTT\n\n"
            for i in range(size):
                # Ensure each cue is 1 second and properly formatted
                content += (
                    f"00:00:{i // 60:02d}.{i % 60:03d} --> "
                    f"00:00:{(i + 1) // 60:02d}.{(i + 1) % 60:03d}\n"
                    f"Cue {i}\n\n"
                )

            start_time = time.time()
            webvtt = parser.parse(content)
            parse_time = time.time() - start_time
            times.append(parse_time)

            assert len(webvtt.cues) == size

        # Verify roughly linear scaling (allowing some variance)
        ratios = [times[i + 1] / times[i] for i in range(len(times) - 1)]
        for ratio in ratios:
            assert 5 < ratio < 15  # Should scale roughly linearly (10x size ≈ 10x time)

    def test_concurrent_parsing(self, parser):
        """Test concurrent parsing of WebVTT files."""

        def parse_file(content):
            return parser.parse(content)

        # Create 10 different WebVTT contents
        contents = []
        for i in range(10):
            content = f"""WEBVTT

00:00:{i:02d}.000 --> 00:00:{i + 1:02d}.000
Test {i}"""
            contents.append(content)

        with ThreadPoolExecutor(max_workers=4) as executor:
            results = list(executor.map(parse_file, contents))

        assert len(results) == 10
        for i, webvtt in enumerate(results):
            assert len(webvtt.cues) == 1
            assert webvtt.cues[0].text == f"Test {i}"


class TestIntegration:
    """Integration tests for WebVTT parser."""

    def test_file_io(self, parser, tmp_path):
        """Test file I/O with different encodings."""
        # Test UTF-8
        utf8_file = tmp_path / "test_utf8.vtt"
        utf8_content = """WEBVTT

00:00:01.000 --> 00:00:02.000
Hello 世界"""
        utf8_file.write_text(utf8_content, encoding="utf-8")
        with open(utf8_file, "r", encoding="utf-8") as f:
            webvtt = parser.parse(f.read())
        assert "世界" in webvtt.cues[0].text

        # Test UTF-16
        utf16_file = tmp_path / "test_utf16.vtt"
        utf16_content = """WEBVTT

00:00:01.000 --> 00:00:02.000
Hello 世界"""
        utf16_file.write_text(utf16_content, encoding="utf-16")
        with open(utf16_file, "r", encoding="utf-16") as f:
            webvtt = parser.parse(f.read())
        assert "世界" in webvtt.cues[0].text

    def test_stream_handling(self, parser):
        """Test parsing from different stream types."""
        content = """WEBVTT

00:00:01.000 --> 00:00:02.000
Test"""

        # Test StringIO
        stream = StringIO(content)
        webvtt = parser.parse(stream.read())
        assert len(webvtt.cues) == 1

        # Test file object
        with tempfile.NamedTemporaryFile(mode="w", delete=False) as f:
            f.write(content)

        with open(f.name, "r") as file_obj:
            webvtt = parser.parse(file_obj.read())
        assert len(webvtt.cues) == 1

        os.unlink(f.name)

    def test_api_usage_patterns(self, parser):
        """Test different API usage patterns."""
        # Test method chaining
        content = """WEBVTT

00:00:01.000 --> 00:00:02.000
Test"""
        webvtt = WebVTTParser().parse(content)
        assert len(webvtt.cues) == 1

        # Test error propagation
        with pytest.raises(ValueError):
            parser.parse("Invalid content")

        # Test event handling (if implemented)
        events = []

        def on_cue(cue):
            events.append(cue)

        # Assuming the parser supports event handlers
        if hasattr(parser, "on_cue"):
            parser.on_cue = on_cue
            webvtt = parser.parse(content)
            assert len(events) == 1
