import pytest
import os
from playwright.sync_api import sync_playwright
from django.contrib.auth.models import User

@pytest.fixture(scope="session")
def test_user(django_db_setup, django_db_blocker):
    with django_db_blocker.unblock():
        return User.objects.create_user(
            username="testuser", password="Testuser1*")

@pytest.fixture(scope="session")
def browser(test_user):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        yield browser
        browser.close()

@pytest.fixture(scope="session")
def page(browser):
    page = browser.new_page()
    yield page
    page.close()
