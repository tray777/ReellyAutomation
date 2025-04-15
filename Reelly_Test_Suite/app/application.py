from pages.main_page import MainPage
from pages.off_plan_new_page import OffPlanNewPage


class Application:

    def __init__(self, driver):
        self.main_page = MainPage(driver)
        self.off_plan_new_page = OffPlanNewPage(driver)

