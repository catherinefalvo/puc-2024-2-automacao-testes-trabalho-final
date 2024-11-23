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

        # Inicializa os objetos de página
        self.home_page = HomePage(self.driver)
        self.course_page = CoursePage(self.driver)
        self.discipline_page = DisciplinePage(self.driver)

    def teardown_method(self):
        self.driver.quit()

    def test_add_student_and_courses(self):
        # Adiciona um aluno chamado "Catarina"
        self.home_page.add_student("Catarina")
        assert "INFO Adicionado aluno" in self.home_page.get_message()

        # Adiciona três cursos: Psicologia, Arquitetura e Análise de Qualidade
        self.course_page.add_course("Psicologia")
        self.course_page.add_course("Arquitetura")
        self.course_page.add_course("Análise de Qualidade")

        # Inscreve o aluno no curso com ID 1
        self.course_page.subscribe_student_to_course(student_id="1", course_id="1")

        # Adiciona três matérias ao curso com ID 1
        self.discipline_page.add_discipline("Design Avançado", "1")
        self.discipline_page.add_discipline("Gestão de Projetos", "1")
        self.discipline_page.add_discipline("Colaboração em Equipe", "1")

        # Inscreve o aluno nas matérias com IDs 1, 2 e 3
        self.discipline_page.subscribe_student_to_disciplines(student_id="1", discipline_ids=["1", "2", "3"])

        # Verifica se a mensagem de sucesso está presente
        assert "INFO" in self.home_page.get_message()
