import os
from flask import Flask, request, jsonify
from flask_mongoengine import MongoEngine

application = Flask(__name__)

application.config['MONGODB_SETTINGS'] = {
    'username': os.environ['MONGODB_USERNAME'],
    'password': os.environ['MONGODB_PASSWORD'],
    'db': os.environ['MONGODB_DATABASE'],
    'host': os.environ['MONGODB_HOSTNAME'],
    'port': 27017
}


mongo = MongoEngine(application)
#db = mongo.db

@application.route('/')
def index():
    return jsonify(
        status=True,
        message='Welcome to the Dockerized Flask MongoDB app!'
    )

@application.route('/todo')
def todo():
    return jsonify(
        status=True,
        message='Welcome to the Dockerized Flask MongoDB app!'
    )
    # _todos = db.todo.find()
    #
    # item = {}
    # data = []
    # for todo in _todos:
    #     item = {
    #         'id': str(todo['_id']),
    #         'todo': todo['todo']
    #     }
    #     data.append(item)
    #
    # return jsonify(
    #     status=True,
    #     data=data
    # )

@application.route('/todo', methods=['POST'])
def createTodo():
    return jsonify(
        status=True,
        message='Welcome to the Dockerized Flask MongoDB app!'
    )
    # data = request.get_json(force=True)
    # item = {
    #     'todo': data['todo']
    # }
    # db.todo.insert_one(item)
    #
    # return jsonify(
    #     status=True,
    #     message='To-do saved successfully!'
    # ), 201

if __name__ == "__main__":
    ENVIRONMENT_DEBUG = os.environ.get("APP_DEBUG", True)
    ENVIRONMENT_PORT = os.environ.get("APP_PORT", 5000)
    application.run(host='0.0.0.0', port=ENVIRONMENT_PORT, debug=ENVIRONMENT_DEBUG)