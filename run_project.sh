#!/bin/bash

echo "🔁 Activating virtual environment..."
source venv/bin/activate

echo "🐳 Building and starting Docker containers..."
docker-compose up --build -d


echo "📤 Sending task to Flask API..."
curl -X POST http://localhost:5000/create-task \
  -H "Content-Type: application/json" \
  -d '{"repo_url": "https://github.com/username/repo", "intern_id": "intern123"}'

echo "🌐 Preview should be available at: http://localhost:8080"
