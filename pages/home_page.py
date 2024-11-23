from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class HomePage(BasePage):
    """Página inicial, para gerenciamento de alunos."""

    student_name_input = (By.ID, "student-nome")
    student_btn = (By.ID, "student-btn")
    messages = (By.CSS_SELECTOR, ".py-p")
    loading_overlay = (By.ID, "pyscript_loading_splash")

    def add_student(self, name):
        """Adiciona um aluno pelo nome."""
        self.wait.until(EC.invisibility_of_element_located(self.loading_overlay))
        self.wait_and_send_keys(self.student_name_input, name)
        self.wait_and_click(self.student_btn)

    def get_message(self, index=1):
        """Obtém a mensagem pelo índice (1-based)."""
        messages = self.get_elements_text(self.messages)
        return messages[index - 1] if index <= len(messages) else None
