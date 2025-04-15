from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep


class OffPlanNewPage(Page):

    OFF_PLAN_BUTTON = (By.XPATH, "//div[@class='menu-button-text new']/preceding-sibling::div[1]//div[@class='g-menu-text']")
    OFF_PLAN_NEW_PAGE = (By.XPATH, "//button[contains(@class, 'pb-5') and contains(@class, 'transition-all') and contains(text(), 'Off-plan')]")
    SALES_STATUS_DROP_DOWN = (By.XPATH, "//button[contains(@class, 'inline-flex') and contains(@class, 'items-center') and contains(text(), 'Sale Status')]")
    OUT_OF_STOCK_BUTTON = (By.XPATH, "//div[contains(@class, 'h-7') and contains(@class, 'focus:ring-ring') and contains(@class, 'font-semibold') and contains (. , 'Out of Stock')]")
    ALL_PROPERTIES_PARENT = (By.XPATH, "//div[@class='px-4 pt-2 pb-4 grid grid-cols-1 xl:grid-cols-2 gap-4 justify-items-center overflow-auto max-h-[calc(100svh-246px)] md:max-h-[calc(100svh-170px)] h-screen']")
    ALL_PROPERTIES = (By.XPATH, "//div[@class='px-4 pt-2 pb-4 grid grid-cols-1 xl:grid-cols-2 gap-4 justify-items-center overflow-auto max-h-[calc(100svh-246px)] md:max-h-[calc(100svh-170px)] h-screen']//a")
    OUT_OF_STOCK_TAG = (By.XPATH, "//span[@class='absolute top-4 left-4 bg-white text-xs font-semibold px-2 py-1 rounded-lg shadow' and text()='Out of stock']")

    def new_page_side_menu(self, button):
        self.wait_element_clickable_click(self.OFF_PLAN_BUTTON)

    def verify_off_plan_new_page(self):
        self.wait_element_visible(*self.OFF_PLAN_NEW_PAGE)
        assert self.find_element(*self.OFF_PLAN_NEW_PAGE).is_displayed()

    def sales_status_dropdown(self, drop_down):
        self.wait_element_clickable_click(self.SALES_STATUS_DROP_DOWN)

    def out_of_stock(self):
        self.wait_element_clickable_click(self.OUT_OF_STOCK_BUTTON)

    def verify_tag(self, tag):

        all_properties_parent = self.find_element(*self.ALL_PROPERTIES_PARENT)
        last_height = self.driver.execute_script("return arguments[0].scrollHeight", all_properties_parent)

        while True:
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", all_properties_parent)
            sleep(1)
            new_height = self.driver.execute_script("return arguments[0].scrollHeight", all_properties_parent)
            if new_height == last_height:
                break
            last_height = new_height

        all_properties = self.find_elements(*self.ALL_PROPERTIES)

        for current_property in all_properties:
            tag_string = current_property.find_element(*self.OUT_OF_STOCK_TAG).text
            assert tag_string == tag
