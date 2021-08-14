from constants.selectors import Product, Navigation, Cart
from base import Base


class ProductPage(Base):
    def add_to_card(self, product):
        self.wait_for_elements(Product.add_to_card_BTN)
        product = Product.title_product_FIELD % product
        self.wait_for_elements(product)
        # self.driver.execute_script("return window.alert = function(){}")
        # self.driver.execute_script("return addToCart(8)")
        self.click_on_element(Product.add_to_card_BTN)
        self.wait_and_accept_alert()

    def go_to_homepage(self):
        self.wait_for_elements(Navigation.home_BTN)
        self.click_on_element(Navigation.home_BTN)

    def go_to_cart(self):
        self.wait_for_elements(Navigation.cart_BTN)
        self.click_on_element(Navigation.cart_BTN)

    def get_price_of_item(self, item):
        item_price = Cart.price_item_FIELD % item
        self.wait_for_elements(item_price)
        return self.get_text_from_element(item_price)

    def get_total_price(self):
        self.wait_for_elements(Cart.price_total_FIELD)
        return self.get_text_from_element(Cart.price_total_FIELD)

    def get_price_from_modal(self):
        self.wait_for_elements(Cart.price_modal_FIELD)
        return self.get_text_from_element(Cart.price_modal_FIELD)
