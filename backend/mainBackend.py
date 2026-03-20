from flask import Flask, jsonify, request
from flask_cors import CORS
from dotenv import load_dotenv
from pymongo import MongoClient
import os

load_dotenv()

app = Flask(__name__)
CORS(app)

client = MongoClient(os.getenv("MONGO_URI"))
db = client.meuprojeto
projects_collection = db.projects

@app.route('/projects', methods=['GET'])
def get_projects():
    projects = list(projects_collection.find({}, {'_id': 0}))
    return jsonify(projects), 200

@app.route('/projects', methods=['POST'])
def add_project():
    new_project = request.get_json()
    projects_collection.insert_one(new_project)
    new_project.pop('_id', None)
    return jsonify(new_project), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)