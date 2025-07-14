# Employee Management API

A FastAPI-based RESTful API for employee management with authentication capabilities.

## Project Overview

This project provides a robust API for managing employee records with secure authentication using JWT tokens. It's built with FastAPI and supports containerization with Docker for easy deployment.

## Features

- Employee registration system
- Secure authentication with JWT tokens
- Token validation and decoding
- Containerized deployment with Docker
- Database integration

## Tech Stack

- **FastAPI**: Modern, fast web framework for building APIs
- **Python 3.9+**: Core programming language
- **JWT**: For secure authentication
- **MySQL**: Database backend
- **Docker**: Containerization
- **uvicorn**: ASGI server

## Project Structure

```
project_one/
├── app/
│   ├── controllers/
│   │   └── employee.py       # Employee API endpoints
│   ├── database/
│   │   └── database.py       # Database connection and operations
│   ├── models/
│   │   └── employee.py       # Employee data models
│   └── utils/
│       ├── jwt_handler.py    # JWT token management
│       └── response_wrapper.py # Standardized API responses
├── .dockerignore
├── Dockerfile                # Docker configuration
├── docker-compose.yaml       # Docker Compose configuration
├── main.py                   # Application entry point
├── requirements.txt          # Project dependencies
└── README.md                 # This file
```

## API Endpoints

### Base URL
`/api`

### Endpoints

- `POST /api/employee` - Create a new employee
- `POST /api/employee_login` - Authenticate and receive a JWT token
- `POST /api/employee_decode` - Validate and decode a JWT token

## Getting Started

### Prerequisites

- Python 3.9+
- Docker and Docker Compose (for containerized deployment)
- MySQL database

### Local Development Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd project_one
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Configure environment variables:
Create a `.env` file in the app directory with the following variables:
```
DATABASE_URL=mysql+pymysql://user:password@localhost/dbname
JWT_SECRET=your_secret_key
```

5. Run the application:
```bash
uvicorn main:app --reload
```

The API will be available at http://localhost:8000.

### Docker Deployment

1. Build and start the containers:
```bash
docker-compose up -d
```

2. The API will be available at http://localhost:8000.

## Authentication

The API uses JWT token-based authentication:

1. Register a new employee using the `/api/employee` endpoint
2. Login with username and password at `/api/employee_login` to receive a JWT token
3. Use this token in the Authorization header for protected endpoints


