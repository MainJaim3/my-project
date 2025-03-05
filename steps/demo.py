from behave import *
from selenium.common import NoSuchElementException


@given('navego a "dynamic content"')
def step_impl(context):
   driver.get("https://the-internet.herokuapp.com/nested_frames")

@when('pulso en "click here')
def step_impl(context):
   driver.find_element(By.LINK_TEXT, "click here")

@then('sale Mario')
def step_impl(context):
    try:
        avatar_mario = context.driver.find_element(
            By.CSS_SELECTOR, "#"
        )
    except NoSuchElementException as e:
        context.driversave_screenshot("evidencia_error.png")
        raise AssertionError("ErrorNoEstáMario")