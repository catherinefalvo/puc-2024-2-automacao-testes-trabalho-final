from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CoursePage(BasePage):
    """Página para gerenciamento de cursos."""

    course_name_input = (By.ID, "course-nome")
    course_btn = (By.ID, "course-btn")
    student_id_input = (By.ID, "student-id")
    course_id_input = (By.ID, "course-id")
    subscribe_btn = (By.CSS_SELECTOR, ".form-group:nth-child(4) > #course-btn")

    def add_course(self, name):
        """Adiciona um curso pelo nome."""
        self.wait_and_send_keys(self.course_name_input, name)
        self.wait_and_click(self.course_btn)

    def subscribe_student_to_course(self, student_id, course_id):
        """Inscreve um aluno em um curso."""
        self.wait_and_send_keys(self.student_id_input, student_id)
        self.wait_and_send_keys(self.course_id_input, course_id)
        self.wait_and_click(self.subscribe_btn)
