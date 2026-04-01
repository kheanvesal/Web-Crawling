"""Detect whether Playwright Chromium is installed for integration tests."""

import functools


@functools.lru_cache(maxsize=1)
def playwright_chromium_available() -> bool:
    """True if Playwright can launch Chromium (run `playwright install chromium` if False)."""
    try:
        from playwright.sync_api import sync_playwright

        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            browser.close()
        return True
    except Exception:
        return False
