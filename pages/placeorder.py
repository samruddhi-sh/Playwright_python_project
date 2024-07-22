from playwright.sync_api import Page, expect

class PlaceOrder():

    def __init__(self, page : Page):
        self.page = page

    def place_order(self):
        return self.page.get_by_role("button", name="Place Order").click()

    def fill_order_details(self, userData: dict):
        self.page.locator("#name").fill(userData['name'])
        self.page.locator("#country").fill(userData['country'])
        self.page.locator("#city").fill(userData['city'])
        self.page.locator("#card").fill(userData['card'])
        self.page.locator("#month").fill(userData['month'])
        self.page.locator("#year").fill(userData['year'])


    def click_purchase(self):
        return self.page.get_by_role("button", name="Purchase").click()

    def verify_message(self):
        self.purchase_msg = self.page.get_by_text("Thank you for your purchase!")
        return expect(self.purchase_msg).to_be_visible()