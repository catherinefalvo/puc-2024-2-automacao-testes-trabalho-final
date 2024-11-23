from selenium.webdriver.common.by import By

class CoursePage:
    def __init__(self, driver):
        self.driver = driver
        self.student_id_input = (By.ID, "student-id")
        self.course_id_input = (By.ID, "course-id")
        self.subscribe_btn = (By.CSS_SELECTOR, ".form-group:nth-child(4) > #course-btn")
        self.course_name_input = (By.ID, "course-nome")
        self.course_btn = (By.ID, "course-btn")

    # Adiciona um curso pelo nome
    def add_course(self, name):
        self.driver.find_element(*self.course_name_input).click()
        self.driver.find_element(*self.course_name_input).send_keys(name)
        self.driver.find_element(*self.course_btn).click()

    # Inscreve um aluno em um curso, usando IDs de aluno e curso
    def subscribe_student_to_course(self, student_id, course_id):
        self.driver.find_element(*self.student_id_input).send_keys(student_id)
        self.driver.find_element(*self.course_id_input).send_keys(course_id)
        self.driver.find_element(*self.subscribe_btn).click()
