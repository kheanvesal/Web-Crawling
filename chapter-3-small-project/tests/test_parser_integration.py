import sys
import pathlib

import pytest

# Ensure src is on sys.path for direct imports when running from repo root
REPO_ROOT = pathlib.Path(__file__).resolve().parents[1]
SRC_DIR = REPO_ROOT / "src"
TESTS_DIR = REPO_ROOT / "tests"
for _p in (SRC_DIR, TESTS_DIR):
    if str(_p) not in sys.path:
        sys.path.insert(0, str(_p))

from parse.base import BasePageParser
from playwright_check import playwright_chromium_available

URL = "https://www.cnbc.com/2025/07/31/apple-aapl-q3-earnings-report-2025.html"

SKIP_PLAYWRIGHT = pytest.mark.skipif(
    not playwright_chromium_available(),
    reason="Playwright Chromium not installed; run: playwright install chromium",
)


@SKIP_PLAYWRIGHT
def test_pageparser_get_links_with_playwright_real_site(tmp_path):
    parser = BasePageParser()

    result = parser.get_links(URL)

    assert isinstance(result, dict)
    assert result.get("url") == URL
    links = result.get("internal_links")
    assert isinstance(links, list)
    # Should find at least some links on a long article page
    assert len(links) > 5


@SKIP_PLAYWRIGHT
def test_pageparser_get_content_with_playwright_real_site(tmp_path):
    parser = BasePageParser()

    result = parser.get_content(URL)

    assert isinstance(result, dict)
    assert result.get("url") == URL
    assert result.get("title") is not None
    assert result.get("content") is not None
    assert result.get("content_length") > 0