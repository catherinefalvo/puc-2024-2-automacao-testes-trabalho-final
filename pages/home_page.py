from selenium.webdriver.common.by import By

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.student_name_input = (By.ID, "student-nome")
        self.student_btn = (By.ID, "student-btn")
        self.messages = (By.CSS_SELECTOR, ".py-p")

    def add_student(self, name):
        self.driver.find_element(*self.student_name_input).click()
        self.driver.find_element(*self.student_name_input).send_keys(name)
        self.driver.find_element(*self.student_btn).click()

    def get_message(self, index=1):
        return self.driver.find_elements(*self.messages)[index - 1].text
