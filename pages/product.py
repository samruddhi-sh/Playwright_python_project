from playwright.sync_api import Page, expect

class ProductPage():
    def __init__(self, page : Page):
        self.page = page

    def product_item(self, product_name):
        return self. page.get_by_role("link", name=product_name).click()

    def handling_alert(self):
        return self.page.on("dialog", lambda dialog: dialog.accept())

    def add_to_cart(self):
        return self.page.get_by_role("link", name="Add to cart").click()

    def go_to_homepage(self):
        return self.page.get_by_role("link",name="Home").click()

    def got_to_cart(self):
        return self.page.get_by_role("link", name="Cart", exact=True).click()

    def check_productin_cart(self, product_name):
        self.product = self.page.locator(f"//td[contains(text(), '{product_name}')]")
        return expect(self.product).to_be_visible()

