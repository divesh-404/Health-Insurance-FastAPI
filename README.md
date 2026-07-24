# Health Insurance FastAPI

A beginner FastAPI project that calculates a customer's health insurance premium based on age, BMI, smoking status, diabetes, and exercise habits.

## Features

- FastAPI REST API
- Pydantic validation
- BMI calculation
- Risk scoring
- Premium calculation

## Technologies

- Python
- FastAPI
- Pydantic
- Uvicorn

## Installation

```bash
git clone https://github.com/yourusername/Health-Insurance-FastAPI.git

cd Health-Insurance-FastAPI

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt
```

## Run

```bash
uvicorn app:app --reload
```

Visit:

```
http://127.0.0.1:8000/docs
```

## API Endpoint

POST

```
/health-insurance
```