from constants.selectors import Cart
from base import Base
import re


class Cartpage(Base):
    def delete_product(self, product):
        deleted_product = Cart.delete_LINK % product
        self.wait_for_elements(deleted_product)
        self.click_on_element(deleted_product)
        self.wait_for_elements_not_visible(deleted_product)

    def submit_order(self):
        self.wait_for_elements(Cart.place_order_BTN)
        self.click_on_element(Cart.place_order_BTN)

    # only required fields
    def fill_customer_data(self, name, credit_card):
        self.wait_for_elements(Cart.name_modal_FIELD)
        self.send_keys_to_the_element(Cart.name_modal_FIELD, name)
        self.send_keys_to_the_element(Cart.cc_modal_FIELD, credit_card)

    def purchase_order(self):
        self.wait_for_elements(Cart.purchase_BTN)
        self.click_on_element(Cart.purchase_BTN)

    def get_data_from_purchase(self, data):
        self.wait_for_elements(Cart.thank_you_TEXT)
        all = self.get_text_from_element(Cart.thank_you_TEXT)
        regex = "(?<=%s: )\d*" % data
        return re.search(regex, all).group(0)
