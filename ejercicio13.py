import time

from django.contrib.admin.helpers import checkbox
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://the-internet.herokuapp.com/dynamic_controls")

boton_remove = driver.find_element(By.CSS_SELECTOR, "#checkbox-example > button")
boton_add = driver.find_element(By.CSS_SELECTOR, "#checkbox-example > button")


boton_remove.click()

for i in range(10):
    time.sleep(1)
    try:
        checkbox = driver.find_element(By.CSS_SELECTOR, "#checkbox > input[type=checkbox]")
    except NoSuchElementException:
        break


try:
    checkbox = driver.find_element(By.CSS_SELECTOR, "#checkbox > input[type=checkbox]")
    raise AssertionError("sigue estando el checkbox")
except NoSuchElementException:
    pass

boton_add.click()

for i in range(10):
    time.sleep(1)
    try:
        checkbox = driver.find_element(By.CSS_SELECTOR, "#checkbox")
    except NoSuchElementException:
        pass

try:
    checkbox = driver.find_element(By.CSS_SELECTOR, "#checkbox")
except NoSuchElementException:
    raise AssertionError("no esta el checkbox")
