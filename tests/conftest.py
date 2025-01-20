import pytest # type: ignore
from playwright.sync_api import sync_playwright, Page # type: ignore
from pages.loginPage import LoginPage
from utilities.readConfig import ReadConfig

# User credentials
user = {
    "username": ReadConfig.getUsername(),
    "password": ReadConfig.getPassword()
}

# fixture for save user state
@pytest.fixture(scope="session",autouse=True)
def logged_in_context():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()

        page = context.new_page()
        login_page = LoginPage(page)

        # login
        login_page.goto()
        login_page.login(user["username"], user["password"])

        # wait for the user profile loaded
        login_page.wait_for_user()

        # save state to the file
        context.storage_state(path="state.json")
        browser.close()
        return context


# fixture to use user state
@pytest.fixture
def page_from_state():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        # create a context with save state
        context = browser.new_context(storage_state="state.json")
        
        # pass the context
        yield context
        
        # close the browser
        browser.close()

