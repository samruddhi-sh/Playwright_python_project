from playwright.sync_api import Page


URL = "https://www.demoblaze.com/"
class  HomePage:
       URL = "https://www.demoblaze.com/"
       def __init__(self, page: Page):
              self.page = page
              self.username = page.locator("#loginusername")
              self.password = page.locator("#loginpassword")
              self.login = page.get_by_role("button", name="Log in")

       def load(self) -> None:
              self.page.goto(self.URL)

       def enter_login_details(self, username, password):
              self.username.fill(username)
              self.password.fill(password)

       def click_login(self):
              self.login.click()