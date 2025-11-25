# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to build and test RESTful APIs using the FastAPI framework in Python. Students will create endpoints, handle requests, and return JSON responses.

## 📝 Tasks

### 🛠️ Create a Simple FastAPI App

#### Description
Set up a basic FastAPI application with at least one endpoint that returns a JSON response.

#### Requirements
Completed program should:
- Use FastAPI to create a web server
- Define a root endpoint (`/`) that returns a welcome message in JSON
- Run locally and respond to HTTP GET requests

### 🛠️ Add CRUD Endpoints

#### Description
Expand your FastAPI app to support Create, Read, Update, and Delete operations for a simple resource (e.g., items, users).

#### Requirements
Completed program should:
- Implement endpoints for creating, reading, updating, and deleting a resource
- Use Python data structures (e.g., list or dict) to store data in memory
- Return appropriate status codes and JSON responses

### 🛠️ (Optional) Add Data Validation

#### Description
Use FastAPI's Pydantic models to validate incoming request data.

#### Requirements
Completed program should:
- Define a Pydantic model for your resource
- Validate request data for create/update operations
- Return error messages for invalid data
