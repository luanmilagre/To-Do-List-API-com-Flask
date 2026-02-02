from flask import Flask, request, jsonify
from models import db, Todo
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

@app.route('/todos', methods=['POST'])
def create_todo():
    data = request.get_json()
    title = data.get('title')

    new_todo = Todo(title=title)
    db.session.add(new_todo)
    db.session.commit()

    return jsonify({'message': 'Todo created'}), 201

@app.route('/todos', methods=['GET'])
def get_todos():
    todos = Todo.query.all()
    todos_list = [{'id': todo.id, 'title': todo.title, 'done': todo.done} for todo in todos]
    return jsonify(todos_list)

@app.route('/todos/<int:todo_id>', methods=['PUT'])
def update_todo(todo_id):
    todo = Todo.query.get(todo_id)
    if not todo:
        return jsonify({'message': 'Todo not found'}), 404

    data = request.get_json()
    todo.title = data.get('title')
    todo.done = data.get('done')
    db.session.commit()

    return jsonify({'message': 'Todo updated'})

@app.route('/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    todo = Todo.query.get(todo_id)
    if not todo:
        return jsonify({'message': 'Todo not found'}), 404

    db.session.delete(todo)
    db.session.commit()

    return jsonify({'message': 'Todo deleted'})

if __name__ == '__main__':
    app.run(debug=True)
