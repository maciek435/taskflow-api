from fastapi import FastAPI
from app.routers import users

app = FastAPI()

app.include_router(users.router, prefix="/users", tags=["users"])

@app.get("/")
def read_root():
    return {"message": "TaskFlow API", "version": "0.1.0"}