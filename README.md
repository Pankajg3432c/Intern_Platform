# 🚀 Intern Platform (DevOps Automation Project)

A lightweight DevOps-based platform that allows automatic cloning, testing, and previewing of intern-submitted GitHub repositories — all containerized with Docker.


## 🧰 Tech Stack

- 🐍 Python + Flask (Backend API)
- 🐳 Docker & Docker Compose (Container Orchestration)
- 🌐 NGINX (Static Preview Server)
- 🧪 (Optional) Pytest-based Test Runner (Future scope)

---

## 🎯 Project Overview

This platform helps automate the following:

1. Clone intern's GitHub repository using a POST request.
2. Store code in a unique workspace folder.
3. If `index.html` is present, move it to the `preview/` folder.
4. NGINX serves the preview on `http://localhost:8080/intern123.html`.
