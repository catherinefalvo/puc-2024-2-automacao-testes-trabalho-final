from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.student_name_input = (By.ID, "student-nome")
        self.student_btn = (By.ID, "student-btn")
        self.messages = (By.CSS_SELECTOR, ".py-p")

    def add_student(self, name):
        wait = WebDriverWait(self.driver, 10)
        
        # Aguarda o campo "student-nome" estar clicável
        student_name_input = wait.until(EC.element_to_be_clickable(self.student_name_input))
        student_name_input.click()
        student_name_input.send_keys(name)

        # Aguarda e clica no botão "Adicionar Aluno"
        student_btn = wait.until(EC.element_to_be_clickable(self.student_btn))
        student_btn.click()
