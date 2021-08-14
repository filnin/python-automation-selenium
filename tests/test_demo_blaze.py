from __future__ import absolute_import
from base import BaseLoggedIn
from pages.homepage import Homepage
from pages.cartpage import Cartpage
from pages.productpage import ProductPage


class TestDemoBlaze(BaseLoggedIn, Homepage, Cartpage, ProductPage):
    def test_add_to_cart_flow(self):
        self.setUp()
        self.go_to_section("Laptops")
        self.select_item("Sony vaio i5")
        self.add_to_card("Sony vaio i5")
        self.go_to_homepage()
        self.go_to_section("Laptops")
        self.select_item("Dell i7 8gb")
        self.add_to_card("Dell i7 8gb")
        self.go_to_cart()
        self.delete_product("Dell i7 8gb")
        total = self.get_total_price()
        self.assertEqual(
            self.get_price_of_item("Sony vaio i5"),
            total
        )
        self.submit_order()
        self.assertIn(
            total,
            self.get_price_from_modal(), "Expected total from modal"
        )
        self.fill_customer_data("Ivan", "41111111etc")
        self.purchase_order()
        final_amount = self.get_data_from_purchase( "Amount")
        self.assertEqual(
            total,
            final_amount, "Asserting final amount"
        )
        print("The id of order is " + self.get_data_from_purchase("Id"))
