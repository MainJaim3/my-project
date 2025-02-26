


"https://the-internet.herokuapp.com/login"

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/login")


   tbx__username_master = driver.find_element(By.ID, value:"username")
   tbx__username.send_keys("tomsmith")

   tbx__password = driver.find_element(By.ID, value: "password")
   tbx__password.send_keys("SuperSecretPassword!")

   driver.find_element(By.CSS_SELECTOR, value: "button").click()

   driver.save_screenshot("screenshot.png")

finally:
driver.quit()

