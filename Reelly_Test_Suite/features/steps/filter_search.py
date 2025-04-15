from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep


@when("click the {button} button")
def new_page_side_menu(context, button):
    context.app.off_plan_new_page.new_page_side_menu(button)


@then('Verify user is on the Off-plan New page')
def verify_off_plan_new_page(context):
    context.app.off_plan_new_page.verify_off_plan_new_page()


@when('Click {drop_down} menu locator')
def sales_status_dropdown(context, drop_down):
    context.app.off_plan_new_page.sales_status_dropdown(drop_down)


@when('Click Out of Stock button')
def out_of_stock(context):
    context.app.off_plan_new_page.out_of_stock()


@then('Verify each product picture contains {tag} tag')
def verify_tag(context, tag):
    context.app.off_plan_new_page.verify_tag(tag)




