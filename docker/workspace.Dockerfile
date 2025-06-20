FROM python:3.9-slim

WORKDIR /workspace

COPY task_manager/workspaces/intern123/ /workspace/

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
