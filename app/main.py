# import os
from database import Profile, Measurements
import datetime

from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi

app = FastAPI()


@app.get("/get/")
async def get(user: int):
    return {}


@app.get("/put/")
async def put(user_id: str, value: int):
    Profile.get_or_create(user_id=user_id)
    profile = Profile.get(user_id=user_id)
    Measurements.get_or_create(
        profile=profile,
        value=int(value)
    )
    return {}


@app.get("/users/")
async def get_all_users():
    return []


def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Custom title",
        version="2.5.0",
        description="This is a very custom OpenAPI schema",
        routes=app.routes,
    )
    openapi_schema["paths"]["/api/auth"] = {
        "post": {
            "requestBody": {"content": {"application/json": {}}, "required": True}, "tags": ["Auth"]
        }
    }
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi
