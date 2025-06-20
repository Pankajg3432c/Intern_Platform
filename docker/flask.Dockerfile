# 1. Base image
FROM python:3.9-slim

# 2. Set working directory
WORKDIR /app

# 3. Install git
RUN apt-get update && apt-get install -y git && rm -rf /var/lib/apt/lists/*

# 4. Copy Flask app files
COPY task_manager/ .

# 5. Install required Python packages
RUN pip install Flask GitPython

# 6. Expose port and run app
EXPOSE 5000

CMD ["python", "main.py"]
