from playwright.sync_api import Page, Playwright
import pytest

@pytest.fixture()
def chromium_page(playwright: Playwright) -> Page:
    browser = playwright.chromium.launch(headless=False)
    yield browser.new_page()
    browser.close()