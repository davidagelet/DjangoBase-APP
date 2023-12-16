# DjangoBase-APP - Product Management API

## Overview
This Django project provides a RESTful API for managing products. It includes functionalities to create, retrieve, update, and delete product information.

## Features
- User authentication and authorization.
- CRUD operations for products.
- RESTful API endpoints.

## Installation and Setup

### Prerequisites
- Python 3.8 or later
- Django 3.2 or later
- Django REST Framework

### Setting Up the Project
1. Clone the repository:
   ```bash
   git clone [repository-url]
   ```

2. Navigate to the project directory:
   ```bash
   cd [project-name]
   ```

3. Create a virtual environment:
   ```bash
   python -m venv venv
   ```

4. Activate the virtual environment:
   - Windows:
     ```bash
     .\venv\Scripts\activate
     ```
   - Unix or MacOS:
     ```bash
     source venv/bin/activate
     ```

5. Install the requirements:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Server
To run the Django development server:

```bash
python manage.py runserver
```

The API will be available at `http://localhost:8000/app/`.

## API Endpoints
- `/valerdat/products/` - GET to retrieve all products, POST to create a new product.
- `/valerdat/products/<id>/` - GET, PUT, and DELETE for retrieving, updating, and deleting a specific product.
- `/valerdat/shearchcoords?product=<product.name>` - Return the product with the longest name from the set of product names.

## Running Tests
To run automated tests:

```bash
python manage.py test app.tests
```