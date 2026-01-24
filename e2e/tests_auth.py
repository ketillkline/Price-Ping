from .conftest import page, test_user

url = "http://127.0.0.1:8000/"

def test_login_page_loads(page):
    page.goto(url + "login/")
    assert page.title != ""