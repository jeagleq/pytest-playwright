# pageObjects/loginPage.py
from playwright.sync_api import Page # type: ignore
from utilities.readConfig import ReadConfig

class LoginPage:
    url = f"{ReadConfig.getApplicationURL()}"
    # Locators 
    textbox_username_id = '#loginusername'
    textbox_password_id = '#loginpassword'
    btn_login_link = '#login2'
    btn_logout_link = '#logout2'
    btn_login  ='button[onclick="logIn()"]'

    # Initiating locators
    def __init__(self, page: Page) -> None:
        self.page = page
        self.username_field = self.page.locator(self.textbox_username_id)
        self.password_field = self.page.locator(self.textbox_password_id)
        self.login_btn_link = self.page.locator(self.btn_login_link)
        self.logout_btn_link = self.page.locator(self.btn_logout_link)
        self.login_btn = self.page.locator(self.btn_login)

    def goto(self) -> None:
        url = self.url
        self.page.goto(url)
    
    def login(self, username: str, password: str) -> None:
        self.login_btn_link.click()
        self.username_field.fill(username)
        self.password_field.fill(password)
        self.login_btn.click()
    
    def wait_for_user(self):
        self.page.wait_for_selector("#nameofuser")