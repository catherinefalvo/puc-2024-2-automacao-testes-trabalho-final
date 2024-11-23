import pytest
from selenium import webdriver
import time
from pages.home_page import HomePage
from pages.course_page import CoursePage
from pages.discipline_page import DisciplinePage


class TestDemo:
    def setup_method(self):
        """Configura o driver do navegador e inicializa as páginas."""
        self.driver = webdriver.Chrome()
        self.driver.get("https://tdd-detroid.onrender.com")
        self.driver.set_window_size(1024, 768)
        self.setup_pages()

    def teardown_method(self):
        """Fecha o navegador após cada teste."""
        self.driver.quit()

    def setup_pages(self):
        """Inicializa os objetos de página."""
        self.home_page = HomePage(self.driver)
        self.course_page = CoursePage(self.driver)
        self.discipline_page = DisciplinePage(self.driver)

    def test_add_student_and_courses(self):
        """Testa a adição de uma aluna, cursos e disciplinas."""
        # Adiciona uma aluna
        self.home_page.add_student("Catherine")
        message = self.home_page.get_message()
        assert "INFO Added student" in message, f"Mensagem inesperada: {message}"
        time.sleep(2)

        # Adiciona três cursos
        for course in ["QA", "Arquitetura", "Psicologia"]:
            self.course_page.add_course(course)
        time.sleep(2)

        # Inscreve a aluna no curso com ID 1
        self.course_page.subscribe_student_to_course(student_id="1", course_id="1")
        time.sleep(2)

        # Adiciona três matérias ao curso com ID 1
        for discipline in ["Page Objects", "Screenplay", "Gherkin"]:
            self.discipline_page.add_discipline(discipline, "1")
        time.sleep(2)

        # Inscreve a aluna nas matérias com IDs 1, 2 e 3
        self.discipline_page.subscribe_student_to_disciplines(
            student_id="1", discipline_ids=["1", "2", "3"]
        )
        time.sleep(2)

        # Verifica se a mensagem de sucesso está presente
        message = self.home_page.get_message()
        assert "INFO" in message, f"Mensagem inesperada após inscrição: {message}"
