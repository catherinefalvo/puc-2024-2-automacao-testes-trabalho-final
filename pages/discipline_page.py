from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class DisciplinePage(BasePage):
    """Página para gerenciamento de disciplinas."""

    discipline_name_input = (By.ID, "discipline-nome")
    course_discipline_id_input = (By.ID, "course-discipline-id")
    add_discipline_btn = (By.CSS_SELECTOR, ".form-group:nth-child(5) > #course-btn")
    student_id_input = (By.ID, "subscribe-student-id")
    discipline_id_input = (By.ID, "subscribe-discipline-id")
    subscribe_btn = (By.CSS_SELECTOR, ".form-group:nth-child(6) > #course-btn")

    def add_discipline(self, name, course_id):
        """Adiciona uma disciplina pelo nome e ID do curso."""
        self.wait_and_send_keys(self.discipline_name_input, name)
        self.wait_and_send_keys(self.course_discipline_id_input, course_id)
        self.wait_and_click(self.add_discipline_btn)

    def subscribe_student_to_disciplines(self, student_id, discipline_ids):
        """Inscreve um aluno em várias disciplinas."""
        for discipline_id in discipline_ids:
            self.wait_and_send_keys(self.student_id_input, student_id)
            self.wait_and_send_keys(self.discipline_id_input, discipline_id)
            self.wait_and_click(self.subscribe_btn)
