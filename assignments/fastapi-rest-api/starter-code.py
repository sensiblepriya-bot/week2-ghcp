# Starter code for FastAPI REST API assignment

"""
This file provides a basic FastAPI setup. Complete the tasks in README.md to build your API.
"""

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to your FastAPI REST API!"}

# Add more endpoints below for CRUD operations

# Example:
# @app.post("/items/")
# def create_item(item: dict):
#     ...

# Remember to validate input and handle errors
