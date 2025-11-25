# Starter code for FastAPI REST API assignment

# main.py
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to your FastAPI API!"}

# Add more endpoints below for CRUD operations
