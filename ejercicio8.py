


class CheckboxesPage(object)

    def __init__(self, driver):
        self.driver = driver
        self.checkbox1 = lambda: driver.find_element(By.CSS_SELECTOR, "#checkboxes > input[type=checkbox]:nth-child(1)")
        self.checkbox2 = lambda: driver.find_element(By.CSS_SELECTOR, "#checkboxes > input[type=checkbox]:nth-child(3)")

driver = webdrive.Chrome()

driver.get("https://the-internet.herokuapp.com/checkboxes")

pagina = CheckboxesPage(driver)


def marcar_checkboxes(chk1, chk2):
    if chk1 and not pagina.esta_checkbox1().is_selected():
        pagina.checkbox1().click()
    if not chk1 and pagina.dame_checkbox1()




marcar_checkboxes(chk1: False, chk2: False)