from contextlib import asynccontextmanager
from random import randint

from fastapi import FastAPI


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield

app = FastAPI(lifespan=lifespan)


@app.get("/")
async def get_random_number():
    return {"numer": randint(1, 50)}
