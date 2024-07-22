import pytest
from playwright.sync_api import Playwright, Page

@pytest.fixture(autouse=True)
def setting_up_teardown(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False, slow_mo=1000)
    page = browser.new_page()
    yield page
    browser.close()