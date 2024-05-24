# Data Pusher Django Application

## Overview

Data Pusher is a Django web application that allows you to create accounts and manage destinations. It receives JSON data via POST requests and forwards this data to multiple destinations (webhook URLs) associated with an account.

## Features

- Create, retrieve, update, and delete accounts.
- Create, retrieve, update, and delete destinations for each account.
- Handle incoming JSON data and forward it to specified destinations based on the account's secret token.
- Support for multiple HTTP methods (GET, POST, PUT) for destinations.

## Installation

### Prerequisites

- Python 3.8+
- Django 3.2+
- Django REST Framework

### Steps

1. **Clone the repository:**

    ```bash
    git clone https://github.com/arshbhatia8/data-pusher.git
    cd data-pusher
    ```

2. **Create a virtual environment and activate it:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. **Install the required packages:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Apply migrations:**

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5. **Run the development server:**

    ```bash
    python manage.py runserver
    ```

## Usage

### API Endpoints

#### Account Endpoints

- **Create an Account:**

    ```http
    POST /api/accounts/
    ```

    **Request Body:**

    ```json
    {
        "email": "user@example.com",
        "account_name": "User Account",
        "website": "https://example.com"
    }
    ```

- **Retrieve, Update, Delete an Account:**

    ```http
    GET /api/accounts/{id}/
    PUT /api/accounts/{id}/
    DELETE /api/accounts/{id}/
    ```

#### Destination Endpoints

- **Create a Destination:**

    ```http
    POST /api/destinations/
    ```

    **Request Body:**

    ```json
    {
        "account": 1,
        "url": "https://webhook.site/your-webhook-url",
        "http_method": "POST",
        "headers": {
            "APP_ID": "1234APPID1234",
            "APP_SECRET": "enwdj3bshwer43bjhjs9ereuinkjcnsiurew8s",
            "ACTION": "user.update",
            "Content-Type": "application/json",
            "Accept": "*"
        }
    }
    ```

- **Retrieve, Update, Delete a Destination:**

    ```http
    GET /api/destinations/{id}/
    PUT /api/destinations/{id}/
    DELETE /api/destinations/{id}/
    ```

#### Data Handler Endpoint

- **Handle Incoming Data:**

    ```http
    POST /api/data/
    ```

    **Request Headers:**

    ```http
    CL-X-TOKEN: your-app-secret-token
    ```

    **Request Body:**

    ```json
    {
        "key": "value"
    }
    ```

    This endpoint identifies the account based on the `CL-X-TOKEN` header, and forwards the incoming JSON data to all destinations associated with the account.

