import time
from dotenv import load_dotenv
import os
from playwright.sync_api import Playwright, Page, expect
from pages.homepage import HomePage

load_dotenv()
username = os.getenv('LOGIN_USERNAME')
password = os.getenv('LOGIN_PASSWORD')

list_products = ['Samsung galaxy s6', 'Nexus 6', 'Nokia lumia 1520']


def test_login(setting_up_teardown):
    """
    Verifies if user is able to log in to application
    :param setting_up_teardown: pytest fixture
    """
    page = setting_up_teardown
    page_object = HomePage(page)
    page_object.load()
    expect(page).to_have_title("STORE")
    page.get_by_role("link", name="Log in").click()
    page_object.enter_login_details(username, password)
    page_object.click_login()
    expect(page.locator("#nameofuser")).to_have_text("Welcome playtest")


def test_add_product(setting_up_teardown):
    """
    Verifies if user is able to add product to cart
    :param setting_up_teardown: pytest fixture
    """
    page = setting_up_teardown
    page_object = HomePage(page)
    page_object.load()
    page.get_by_role("link", name="Samsung galaxy s6").click()
    page.on("dialog", lambda dialog: dialog.accept())
    page.pause()
    page.get_by_role("link", name="Add to cart").click()
    page.get_by_role("link", name="Cart", exact=True).click()
    product = page.locator("//td[contains(text(), 'Samsung galaxy')]")
    expect(product).to_be_visible()
    product.screenshot(path="Screenshots/product_cart.png")


def test_add_multiple_products(setting_up_teardown):
    """
    Verifies if multiple products can be added to cart
    :param setting_up_teardown: pytest fixture
    """
    page = setting_up_teardown
    page_object = HomePage(page)
    page_object.load()
    for a in list_products:
        page.get_by_role("link", name=a).click()
        page.on("dialog", lambda dialog: dialog.accept())
        page.get_by_role("link", name="Add to cart").click()
        time.sleep(2)
        page.get_by_role("link", name="Home").click()
    page.get_by_role("link", name="Cart", exact=True).click()
    for a in list_products:
        product = page.locator(f"//td[contains(text(), '{a}')]")
        expect(product).to_be_visible()
    table = page.locator("div.table-responsive")
    table.screenshot(path="Screenshots/cart.png")
