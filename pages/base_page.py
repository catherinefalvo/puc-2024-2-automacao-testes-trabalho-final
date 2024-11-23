from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    """Classe base para páginas, com métodos comuns."""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def wait_and_click(self, locator):
        """Espera o elemento estar clicável e clica."""
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def wait_and_send_keys(self, locator, keys):
        """Espera o elemento estar clicável e insere texto."""
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.clear()
        element.send_keys(keys)

    def get_elements_text(self, locator):
        """Retorna o texto de todos os elementos localizados."""
        return [el.text for el in self.driver.find_elements(*locator)]
