
Este projeto consiste em uma **API** de lista de tarefas (To-Do List) desenvolvida com **Flask** e **SQLAlchemy**. Ele permite que os usuários criem, atualizem, marquem como concluídas e excluam tarefas. A ideia principal deste projeto é entender como criar um CRUD básico utilizando Flask com um banco de dados relacional.

## Funcionalidades

- **Criar tarefa**: Adiciona uma nova tarefa à lista.
- **Listar tarefas**: Exibe todas as tarefas.
- **Atualizar tarefa**: Permite marcar uma tarefa como concluída ou atualizar seu título.
- **Excluir tarefa**: Exclui uma tarefa da lista.

## Tecnologias Usadas

- **Python** 3.x
- **Flask** (Web Framework)
- **SQLAlchemy** (ORM para interação com o banco de dados)
- **SQLite** (Banco de dados relacional simples para desenvolvimento)

## Instalação

### 1. Clone o repositório:

```bash
git clone https://github.com/luanmilagre/To-Do-List-API-com-Flask/pull/new/master
cd todo-list-flask
2. Crie um ambiente virtual e ative-o:
No Windows:
python -m venv venv
.\venv\Scripts\activate

No Linux/MacOS:
python3 -m venv venv
source venv/bin/activate

3. Instale as dependências:
pip install -r requirements.txt

4. Crie o banco de dados:
flask db init
flask db migrate
flask db upgrade

Como Usar
1. Inicie a aplicação Flask:
python app.py


A aplicação estará disponível em http://127.0.0.1:5000/.

2. Teste as rotas da API usando o Postman ou cURL:

POST /todos: Cria uma nova tarefa.

GET /todos: Lista todas as tarefas.

PUT /todos/{id}: Atualiza o status ou título da tarefa.

DELETE /todos/{id}: Exclui uma tarefa.

Exemplos de Uso
Criar Tarefa (POST):

URL: http://127.0.0.1:5000/todos

Body (JSON):

{
  "title": "Estudar Flask"
}

Listar Tarefas (GET):

URL: http://127.0.0.1:5000/todos

Atualizar Tarefa (PUT):

URL: http://127.0.0.1:5000/todos/1

Body (JSON):

{
  "title": "Estudar Flask - Aula 2",
  "done": true
}

Excluir Tarefa (DELETE):

URL: http://127.0.0.1:5000/todos/1
