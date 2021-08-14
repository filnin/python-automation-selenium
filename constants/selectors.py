class Home(object):
    product_name_FIELD = "//a[contains(.,'%s')]"
    section_name_FIELD = "//a[contains(.,'%s')]"


class Cart(object):
    delete_LINK = "(//td[contains(text(),'%s')]/following::a)[1]"
    price_total_FIELD = '#totalp'
    price_item_FIELD = "(//td[contains(text(),'%s')]/following::td)[1]"
    place_order_BTN = "//button[contains(.,'Place Order')]"
    # modal window
    price_modal_FIELD = "#totalm"
    name_modal_FIELD = "#name"
    cc_modal_FIELD = "#card"
    purchase_BTN = "//button[contains(.,'Purchase')]"
    thank_you_TEXT = "//div[@class='sa-icon sa-success animate']/following::p"


class Product(object):
    add_to_card_BTN = "//a[contains(.,'Add to cart')]"
    title_product_FIELD = "//h2[contains(.,'%s')]"
    single_price_cart_FIELD = "(//p[@class='a-spacing-small']/span)[1]"


class Navigation(object):
    home_BTN = "//a[contains(text(),'Home')]"
    cart_BTN = "//a[contains(text(),'Cart')]"
