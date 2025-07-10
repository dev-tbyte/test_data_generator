# Test Data Generator API

This is a Python web project built with FastAPI that provides a REST API for generating various types of test data based on user-defined settings. It includes Swagger (OpenAPI) support for easy interaction and documentation.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Setup and Usage](#setup-and-usage)
  - [1. Navigate to the project directory](#1-navigate-to-the-project-directory)
  - [2. Create and Activate a Virtual Environment](#2-create-and-activate-a-virtual-environment)
  - [3. Install Dependencies](#3-install-dependencies)
  - [4. Run the Application](#4-run-the-application)
- [Accessing the API](#accessing-the-api)
  - [Using the Swagger UI](#using-the-swagger-ui)
  - [Using curl](#using-curl)
- [API Endpoint](#api-endpoint)
  - [POST /generate-data](#post-generate-data)
- [Building and Running a Standalone Executable](#building-and-running-a-standalone-executable)
  - [1. Install PyInstaller and PyArmor](#1-install-pyinstaller-and-pyarmor)
  - [2. Obfuscate and Package Your Code](#2-obfuscate-and-package-your-code)
  - [3. Run the Executable](#3-run-the-executable)
- [Important Considerations for Code Protection](#important-considerations-for-code-protection)

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

### 2. Create and Activate a Virtual Environment

It's highly recommended to use a virtual environment to manage project dependencies.

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies

With the virtual environment activated, install the required Python packages:

```bash
pip install -r requirements.txt
```

### 4. Run the Application

Start the FastAPI application using Uvicorn. For development, you might use `--reload`. For production, remove `--reload`.

```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```

## Accessing the API

### Using the Swagger UI

Once the application is running, you can access the interactive Swagger UI at:

[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

From the Swagger UI, you can explore the `/generate-data` endpoint, understand its request body structure, and test data generation directly from your browser.

### Using curl

You can also interact with the API using `curl` from your terminal. Here is an example of how to generate test data:

```bash
curl -X 'POST' \
  'http://127.0.0.1:8000/generate-data' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "num_records": 2,
  "fields": [
    {
      "name": "id",
      "type": "uuid"
    },
    {
      "name": "full_name",
      "type": "name"
    },
    {
      "name": "contact_email",
      "type": "email"
    }
  ]
}'
```

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

## Building and Running a Standalone Executable

To distribute your application as a single executable file that doesn't require the client to install Python or its dependencies, and to make your code harder to read and understand, you can use `PyInstaller` in conjunction with a code obfuscator like `PyArmor`.

### 1. Install PyInstaller and PyArmor

First, activate your virtual environment and install both PyInstaller and the latest version of PyArmor:

```bash
source .venv/bin/activate
pip install pyinstaller pyarmor
```

### 2. Obfuscate and Package Your Code

PyArmor integrates with PyInstaller to simplify the process of obfuscating and packaging your application. The following command will obfuscate your script and then package it using PyInstaller.

```bash
pyarmor gen --pack onefile main.py
```

**Explanation of the command:**
*   `pyarmor gen`: This is the PyArmor command to generate obfuscated scripts.
*   `--pack onefile`: This tells PyArmor to package the output as a single executable file using PyInstaller.
*   `main.py`: This is the entry point of your application.

This command will create a `dist` directory containing the final executable file.

### 3. Run the Executable

You can run the generated executable directly from the `dist` directory:

```bash
./dist/main
```

The application will start, and you can access the API as usual.

### Important Considerations for Code Protection

*   **Obfuscation is a Deterrent, Not a Guarantee:** While obfuscation makes your code significantly harder to read and understand, it is not foolproof. A highly determined and skilled reverse engineer might still be able to de-obfuscate the code.
*   **Testing is Crucial:** Obfuscation can sometimes introduce subtle issues. Always thoroughly test your obfuscated and packaged application to ensure all functionalities work as expected.
*   **Licensing and Legal Agreements:** The most robust protection for your intellectual property comes from strong licensing agreements and legal frameworks, rather than relying solely on technical measures.
*   **API-based Distribution (Most Secure):** If feasible, the most secure way to protect your core logic is to host the API on your own servers and provide clients with access to the API endpoints. This keeps your source code entirely on your controlled infrastructure.
