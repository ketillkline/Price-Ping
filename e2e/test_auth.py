from django.contrib.auth.models import User
from .conftest import page, raw_password


url = "http://127.0.0.1:8000/"

def test_login_page_loads(page):
    page.goto(url + "login/")
    assert page.title != ""

def test_login(page):
    page.goto(url + "login/")
    page.fill("input[name='username']", "testuser")
    page.fill("input[name='password']", raw_password)

    page.click("button[type='submit']")

    assert page.title() == "Dashboard"