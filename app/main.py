
import os

import psycopg
from fastapi import FastAPI
from psycopg.rows import dict_row

app = FastAPI(title="DevOps CI/CD Project")

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://devops:devops@localhost:5432/tasks"
)


@app.get("/")
def home():
    return {
        "message": "Hello from Production CI/CD!",
        "version": os.getenv("APP_VERSION", "local")
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


@app.get("/db-health")
def database_health():
    try:
        with psycopg.connect(DATABASE_URL) as connection:
            with connection.cursor(row_factory=dict_row) as cursor:
                cursor.execute("SELECT 1 AS result")
                result = cursor.fetchone()

        return {
            "database": "connected",
            "result": result["result"]
        }

    except Exception:
        return {
            "database": "unavailable"
        }
