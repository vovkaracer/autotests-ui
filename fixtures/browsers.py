from playwright.sync_api import Page, Playwright
import pytest
from pages.authentication.registration_page import RegistrationPage

@pytest.fixture()
def chromium_page(playwright: Playwright) -> Page:
    browser = playwright.chromium.launch(headless=False)
    yield browser.new_page()
    browser.close()

@pytest.fixture(scope='session')
def initialize_browser_state(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    registration_page = RegistrationPage(page)
    registration_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')

    registration_page.registration_form.fill_form(email='user@mail.ru', username='username', password='password')

    registration_page.click_registration_button()

    context.storage_state(path='browser-state.json')
    browser.close()

@pytest.fixture()
def chromium_page_with_state(initialize_browser_state, playwright: Playwright) -> Page:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state='browser-state.json')
    yield context.new_page()
    browser.close()