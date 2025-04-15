from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep


@given("Open Reelly main page")
def open_reelly_main_page(context):
    context.app.main_page.open_reelly_main_page()


@when("Type user email {email} into email textbox")
def user_email_textbox(context, email):
    context.app.main_page.user_email_textbox(email)


@when("Type user password {password} into password textbox")
def user_password_textbox(context, password):
    context.app.main_page.user_password_textbox(password)


@when("Click Continue button")
def click_continue_button(context):
    context.app.main_page.click_continue_button()


@then("Verify user is on the login page")
def verify_user_is_on_login_page(context):
    context.app.main_page.verify_user_is_on_login_page()


@then("Verify that {main_menu_button} text is displayed")
def verify_text_displayed(context, main_menu_button):
    context.app.main_page.verify_text_displayed(main_menu_button)
