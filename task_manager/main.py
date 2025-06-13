from flask import Flask, request, jsonify
from git import Repo
import os

app = Flask(__name__)

@app.route('/create-task', methods=['POST'])
def create_task():
    data = request.get_json()
    repo_url = data.get('repo_url')
    intern_id = data.get('intern_id', 'default_user')

    workspace_path = f"./workspaces/{intern_id}"
    if os.path.exists(workspace_path):
        return jsonify({"error": "Workspace already exists"}), 400

    try:
        Repo.clone_from(repo_url, workspace_path)
        return jsonify({"status": "cloned", "path": workspace_path})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
