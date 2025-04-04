FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 8000
RUN touch /app/users.db
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]