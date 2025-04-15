from pages.base_page import Page
from selenium.webdriver.common.by import By
from time import sleep
from behave import given, when, then


class MainPage(Page):
    MAIN_MENU_BUTTON = (By.XPATH, "//div[@class='g-menu-text' and text()='Main menu']")
    CONTINUE_BUTTON = (By.XPATH, "//a[@wized='loginButton']")
    EMAIL_TEXT = (By.XPATH, "//input[@id='email-2']")
    PASSWORD_TEXT = (By.XPATH, "//input[@id='field']")
    VERIFY_LOGIN = (By.XPATH, "//h1[text()='Sign in or create new account']")

    def open_reelly_main_page(self):
        self.open('https://soft.reelly.io/sign-in')

    def user_email_textbox(self, email):
        self.input_text(email, *self.EMAIL_TEXT)

    def user_password_textbox(self, password):
        self.input_text(password, *self.PASSWORD_TEXT)

    def click_continue_button(self):
        self.wait_element_clickable_click(self.CONTINUE_BUTTON)
        #sleep(6)

    def verify_user_is_on_login_page(self):
        verify_page = self.find_element(*self.VERIFY_LOGIN).text
        assert verify_page

    def verify_text_displayed(self, total_projects_text):
        self.wait_element_visible(*self.MAIN_MENU_BUTTON)
        assert self.find_element(*self.MAIN_MENU_BUTTON).is_displayed()





