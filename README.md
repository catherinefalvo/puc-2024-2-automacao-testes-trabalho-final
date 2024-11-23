# Trabalho Final Automação de Testes de Software

Trabalho final da disciplina de Automação de Testes de Software na pós-graduação pela PUC-Minas. Este projeto foi desenvolvido para realizar testes automatizados usando o padrão **Page Objects**, facilitando a manutenção e escalabilidade do código.

### Estrutura de Projeto

```plaintext
/
├── pages/
│   ├── home_page.py          # Page Objects para interações com a Home
│   ├── course_page.py        # Page Objects para interações com Cursos
│   └── discipline_page.py    # Page Objects para interações com Disciplinas
├── tests/
│   ├── test_demo.py          # Casos de teste organizados
├── requirements.txt          # Dependências do projeto
├── README.md                 # Documentação
├── test_final_exercise_raw   # Script base do professor
```

### Padrões Utilizados

1. **Page Objects:**  
   As interações com elementos da interface são encapsuladas em classes específicas, separando a lógica de UI dos testes.

2. **Organização de Código:**  
   Os testes são escritos para simular fluxos reais de uso do sistema.

3. **Reutilização de Código:**  
   Métodos nos Page Objects podem ser usados em múltiplos testes, reduzindo redundâncias.

### Execução

1. **Instalar dependências:**

   Certifique-se de que você possui o Python e o pip instalados. Depois, execute:

   ```bash
   pip install -r requirements.txt
   ```

2. **Executar os testes:**

   Para rodar todos os testes, use o comando:

   ```bash
   pytest tests/
   ```
