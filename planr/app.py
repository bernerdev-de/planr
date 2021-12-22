from fastapi import FastAPI
from planr.routes.auth import router as auth_router
from planr.orm import init
from dotenv import load_dotenv
import os
app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}



app.include_router(auth_router, prefix="")

@app.on_event("startup")
async def startup():
    load_dotenv()
    print("Startup")
    await init()
