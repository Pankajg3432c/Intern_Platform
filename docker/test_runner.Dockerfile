FROM python:3.10
RUN pip install pytest
WORKDIR /app
CMD ["pytest"]
