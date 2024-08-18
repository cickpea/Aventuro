# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.11-slim

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY . /app

EXPOSE 7860

ENV GRADIO_SERVER_NAME="0.0.0.0"

ENTRYPOINT ["python", "main.py"]