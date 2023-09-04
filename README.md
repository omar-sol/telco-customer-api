# telco-customer-api

This project creates a FastAPI app for a telco-customer-churn model.

## Installation

Create a new Python environment

```bash
python -m venv .env
```
Install the dependencies

```bash
pip install -r requirements.txt
```

## Usage
```bash
uvicorn main:app --reload
```

## Create a Docker image
Build the image
```bash
docker build --platform linux/amd64 -t telco .
```
Test the image
```bash
docker run -it --name telco-container -p 80:80 telco
```
Tag the image
```bash
docker tag telco gcr.io/PROJECT_ID/telco:latest
```
Push to Google Container Registry
```bash
docker push gcr.io/PROJECT_ID/telco:latest
```