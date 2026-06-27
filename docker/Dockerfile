FROM python:3.11-slim

WORKDIR /app

COPY fastapi/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY fastapi/app.py .
COPY fastapi/salary_model.pkl .

EXPOSE 8000

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
