"https://the-internet.herokuapp.com/nested_frames"


from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/nested_frames")

driver.switch_to.frame("frame-top")
driver.switch_to.frame("frame-middle")

middle = driver.find_element(By.ID, value: "content")

driver.switch_to.default_content()

