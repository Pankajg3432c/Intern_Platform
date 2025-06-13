FROM python:3.10-slim
RUN useradd -ms /bin/bash intern
USER intern
WORKDIR /home/intern/work
CMD ["sleep", "infinity"]
