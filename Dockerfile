# Use the official fastapi uvicorn image
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application
COPY ./app /app

# If your main file is named app.py, use the following line to start the FastAPI application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]