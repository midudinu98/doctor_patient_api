# doctor_patient_api

Doctor-Patient API Management

A simple REST API built using FastAPI and Pydantic to manage doctors and patients.

The project currently uses in-memory storage, so data is stored temporarily in Python lists while the application is running.

Technologies Used

Python 3.9+
FastAPI
Pydantic
Uvicorn
In-memory storage

Project Structure

doctor_patient_api/
│
├── main.py
└── README.md

Setup Instructions

1. Create a virtual environment
Open the project folder in the terminal:

python -m venv venv

2. Activate the virtual environment

venv\Scripts\activate

3. Install required packages

pip install fastapi uvicorn pydantic email-validator

email-validator is required because the project uses Pydantic's EmailStr.

4. Run the application

If your Python file is named main.py:

uvicorn main:app --reload

The API will start at:

http://127.0.0.1:8000

API Documentation

FastAPI automatically provides interactive Swagger documentation.

Open:

http://127.0.0.1:8000/docs

You can test all API endpoints directly from Swagger UI.

Stopping the Server

To stop the FastAPI server, press:

CTRL + C
