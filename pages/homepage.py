from constants.selectors import Home
from base import Base


class Homepage(Base):

    def select_item(self, brand):
        brand_link = Home.product_name_FIELD % brand
        self.wait_for_elements(brand_link)
        self.click_on_element(brand_link)

    def go_to_section(self, section):
        section_link = Home.section_name_FIELD % section
        self.wait_for_elements(section_link)
        self.click_on_element(section_link)