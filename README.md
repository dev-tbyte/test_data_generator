# Test Data Generator API

This is a Python web project built with FastAPI that provides a REST API for generating various types of test data based on user-defined settings. It includes Swagger (OpenAPI) support for easy interaction and documentation.

## Features

- Generate a specified number of test data records.
- Define custom fields with different data types (string, integer, float, boolean, date, email, phone_number, address, text, uuid, name, word, sentence, paragraph).
- Set constraints for numerical fields (min/max values) and string fields (max length).
- Interactive API documentation via Swagger UI.

## Technologies Used

- **FastAPI**: A modern, fast (high-performance) web framework for building APIs with Python 3.7+ based on standard Python type hints.
- **Pydantic**: Data validation and settings management using Python type hints.
- **Uvicorn**: An ASGI web server for Python.
- **Faker**: A Python package that generates fake data for you.

## Setup and Usage

Follow these steps to set up and run the test data generator:

### 1. Navigate to the project directory

```bash
cd /opt/python-workspace/test_data_generator
```

### 2. Install Dependencies

Install the required Python packages using pip:

```bash
pip install -r requirements.txt
```

### 3. Run the Application

Start the FastAPI application using Uvicorn. The `--reload` flag enables auto-reloading on code changes, which is useful for development.

```bash
uvicorn main:app --reload
```

### 4. Access the API Documentation

Once the application is running, you can access the interactive Swagger UI at:

[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

From the Swagger UI, you can explore the `/generate-data` endpoint, understand its request body structure, and test data generation directly from your browser.

## API Endpoint

### `POST /generate-data`

Generates test data based on the provided settings.

**Request Body Example:**

```json
{
  "num_records": 5,
  "fields": [
    {
      "name": "user_id",
      "type": "uuid"
    },
    {
      "name": "username",
      "type": "name"
    },
    {
      "name": "email",
      "type": "email"
    },
    {
      "name": "age",
      "type": "integer",
      "min_value": 18,
      "max_value": 65
    },
    {
      "name": "description",
      "type": "text",
      "max_length": 200
    }
  ]
}
```

**Response Example:**

```json
{
  "generated_data": [
    {
      "user_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
      "username": "John Doe",
      "email": "john.doe@example.com",
      "age": 30,
      "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
    }
    // ... more records
  ]
}
```
