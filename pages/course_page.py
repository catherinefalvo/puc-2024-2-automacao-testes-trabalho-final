from selenium.webdriver.common.by import By

class CoursePage:
    def __init__(self, driver):
        self.driver = driver
        self.course_name_input = (By.ID, "course-nome")
        self.course_btn = (By.ID, "course-btn")

    def add_course(self, name):
        self.driver.find_element(*self.course_name_input).click()
        self.driver.find_element(*self.course_name_input).send_keys(name)
        self.driver.find_element(*self.course_btn).click()
