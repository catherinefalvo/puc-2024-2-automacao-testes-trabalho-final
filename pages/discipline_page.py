from selenium.webdriver.common.by import By

class DisciplinePage:
    def __init__(self, driver):
        self.driver = driver
        self.discipline_name_input = (By.ID, "discipline-nome")
        self.course_discipline_id_input = (By.ID, "course-discipline-id")
        self.course_btn = (By.CSS_SELECTOR, ".form-group:nth-child(5) > #course-btn")

    def add_discipline(self, name, course_id):
        self.driver.find_element(*self.discipline_name_input).click()
        self.driver.find_element(*self.discipline_name_input).send_keys(name)
        self.driver.find_element(*self.course_discipline_id_input).send_keys(course_id)
        self.driver.find_element(*self.course_btn).click()
