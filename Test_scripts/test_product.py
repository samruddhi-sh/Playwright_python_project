import time

from pages.product import ProductPage
from pages.homepage import HomePage

list_products = ['Samsung galaxy s6', 'Nexus 6', 'Nokia lumia 1520']

def test_product_add(setting_up_teardown):
    """
    Adds multiple products in cart using POM design
    :param setting_up_teardown: pytest fixture
    :return:
    """
    page = setting_up_teardown
    home_page = HomePage(page)
    product_add = ProductPage(page)
    home_page.load()
    for product in list_products:
        product_add.product_item(product)
        product_add.handling_alert()
        product_add.add_to_cart()
        time.sleep(2)
        product_add.go_to_homepage()
    product_add.got_to_cart()
    for product in list_products:
        product_add.check_productin_cart(product)

