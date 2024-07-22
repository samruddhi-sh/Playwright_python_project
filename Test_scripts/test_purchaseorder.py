import time
import os
import json
from dotenv import load_dotenv
from pages.product import ProductPage
from pages.homepage import HomePage
from pages.placeorder import PlaceOrder

load_dotenv()

def get_config():
    """ Gets the user details to place order sensitive
    data is loaded from env variable"""
    # Retrieve the environment variable
    config_json = os.getenv('FORM_DETAILS')

    # Check if the environment variable exists
    if config_json is None:
        raise ValueError("CONFIG environment variable not set")

    # Convert JSON string back to dictionary
    return json.loads(config_json)


def test_purchasing(setting_up_teardown):
    data_dict = get_config()
    page = setting_up_teardown
    home_page = HomePage(page)
    product_add = ProductPage(page)
    placing_order = PlaceOrder(page)
    home_page.load()
    product_add.product_item("Iphone 6 32gb")
    product_add.handling_alert()
    product_add.add_to_cart()
    product_add.got_to_cart()
    placing_order.place_order()
    placing_order.fill_order_details(data_dict)
    placing_order.click_purchase()
    placing_order.verify_message()



