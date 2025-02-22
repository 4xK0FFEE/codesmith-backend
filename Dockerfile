FROM python:3.10-alpine
WORKDIR /app
RUN apk add --no-cache py3-pip
RUN pip install poetry
COPY ./pyproject.toml ./
RUN poetry config virtualenvs.create false && poetry install --no-interaction --no-ansi --only main
COPY ./src ./src
EXPOSE 3000
CMD ["gunicorn", "-w", "4", "-k", "uvicorn.workers.UvicornWorker", "src:app", "--bind", "0.0.0.0:3000"]
