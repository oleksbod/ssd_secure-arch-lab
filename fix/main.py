from __future__ import annotations

import os
import logging
from typing import Annotated

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

logger = logging.getLogger("user-api")
logging.basicConfig(level=os.getenv("LOG_LEVEL", "INFO"))

app = FastAPI(title="user-api", version="1.0.0")


class UserOut(BaseModel):
    id: int
    name: str


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}


@app.get("/user", response_model=UserOut)
def get_user(id: Annotated[int, Field(ge=1)]) -> UserOut:
    # приклад контрольованого контракту (типи + валідація)
    return UserOut(id=id, name="Alice")


class LoginIn(BaseModel):
    password: str = Field(min_length=1)


@app.post("/login")
async def login(payload: LoginIn) -> dict:
    # секрет береться з середовища / secret manager (не з коду)
    expected = os.getenv("APP_LOGIN_SECRET")
    if not expected:
        logger.error("APP_LOGIN_SECRET is not configured")
        raise HTTPException(status_code=500, detail="Misconfigured server")

    if payload.password == expected:
        return {"status": "ok"}

    raise HTTPException(status_code=401, detail="Invalid credentials")
