

from random import randint

from selenium.webdriver.common.by import By


veces = randint(a:1, b:10)


class AddRemovePage(object):


driver.get("https://the-internet.herokuapp.com/login")

    def __init__(self, driver):
        self.driver = driver
        self.add_button = lambda: driver.find_element(By.CSS_SELECTOR, "#content > div > button")
        self.delete_button = lambda: driver.find_element(By.CSS_SELECTOR, "#elements > button")

driver = webdriver.Chrome()

pagina = AddRemovePage(driver)

for i in range(veces)
    pagina.add_button.click()

for i in range(veces)
    pagina.delete_button.click()