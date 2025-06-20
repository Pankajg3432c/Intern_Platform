from flask import Flask, request, jsonify
from git import Repo
import os
import shutil

app = Flask(__name__)

@app.route('/create-task', methods=['POST'])
def create_task():
    data = request.get_json()
    repo_url = data['repo_url']
    intern_id = data.get('intern_id', 'default_user')

    workspace_path = f"./workspaces/{intern_id}"

    if os.path.exists(workspace_path):
        shutil.rmtree(workspace_path)

    try:
        Repo.clone_from(repo_url, workspace_path)
        return jsonify({"status": "cloned", "intern_id": intern_id}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
