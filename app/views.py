from flask import Blueprint, request, jsonify
from . import db
from .models import Task

bp = Blueprint('main', __name__)

@bp.route('/tasks', methods=['GET'])
def get_tasks():
    tasks = Task.query.all()
    return jsonify([{'id': task.id, 'title': task.title, 'description': task.description} for task in tasks])

@bp.route('/tasks', methods=['POST'])
def add_task():
    data = request.get_json()
    new_task = Task(title=data['title'], description=data.get('description'))
    db.session.add(new_task)
    db.session.commit()
    return jsonify({'id': new_task.id, 'title': new_task.title, 'description': new_task.description}), 201

@bp.route('/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):
    task = Task.query.get(id)
    if task is None:
        return jsonify({'message': 'Task não encontrada'}), 404
    db.session.delete(task)
    db.session.commit()
    return jsonify({'messagem': 'Task deletada'})


@bp.route('/test-db', methods=['GET'])
def test_db():
    try:
        test_task = Task(title="Teste de Conexão", description="Esta é uma tarefa de teste.")
        db.session.add(test_task)
        db.session.commit()
        db.session.delete(test_task)
        db.session.commit()
        return jsonify({"message": "Conexão com o banco de dados está funcionando corretamente."}), 200
    except Exception as e:
        return jsonify({"message": f"Erro ao conectar ao banco de dados: {str(e)}"}), 500
