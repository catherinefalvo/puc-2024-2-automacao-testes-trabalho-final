import pytest
from selenium import webdriver
from pages.home_page import HomePage
from pages.course_page import CoursePage
from pages.discipline_page import DisciplinePage

class TestDemo:
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://tdd-detroid.onrender.com")
        self.driver.set_window_size(970, 555)

        # Initialize Page Objects
        self.home_page = HomePage(self.driver)
        self.course_page = CoursePage(self.driver)
        self.discipline_page = DisciplinePage(self.driver)

    def teardown_method(self):
        self.driver.quit()

    def test_add_student_and_courses(self):
        # Add Catherine as a student
        self.home_page.add_student("Catherine")
        assert "INFO Added student" in self.home_page.get_message()

        # Add courses for Catherine
        self.course_page.add_course("Psychology")
        self.course_page.add_course("Architecture")
        self.course_page.add_course("Quality Analysis")

        # Add discipline
        self.discipline_page.add_discipline("Advanced Design", "1")
        assert "FAIL Necessários 3 cursos" in self.home_page.get_message()
