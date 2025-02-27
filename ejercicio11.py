"https://the-internet.herokuapp.com/nested_frames"


from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/javascript_alerts")

drive = webdriver.Chrome()

boton = driver.find_element(By.CSS_SELECTOR, value "#content > div > ul > li:nth-child(1) > button")

alert = driver.switch_to.alert
alert.accept()

