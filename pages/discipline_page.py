from selenium.webdriver.common.by import By

class DisciplinePage:
    def __init__(self, driver):
        self.driver = driver
        self.discipline_name_input = (By.ID, "discipline-nome")
        self.course_discipline_id_input = (By.ID, "course-discipline-id")
        self.course_btn = (By.CSS_SELECTOR, ".form-group:nth-child(5) > #course-btn")
        self.student_discipline_id_input = (By.ID, "subscribe-discipline-id")
        self.subscribe_btn = (By.CSS_SELECTOR, ".form-group:nth-child(6) > #course-btn")

    # Adiciona uma matéria pelo nome e pelo ID do curso
    def add_discipline(self, name, course_id):
        self.driver.find_element(*self.discipline_name_input).click()
        self.driver.find_element(*self.discipline_name_input).send_keys(name)
        self.driver.find_element(*self.course_discipline_id_input).send_keys(course_id)
        self.driver.find_element(*self.course_btn).click()

    # Inscreve um aluno em várias matérias, usando IDs das matérias
    def subscribe_student_to_disciplines(self, student_id, discipline_ids):
        for discipline_id in discipline_ids:
            self.driver.find_element(*self.student_discipline_id_input).send_keys(discipline_id)
            self.driver.find_element(*self.subscribe_btn).click()
