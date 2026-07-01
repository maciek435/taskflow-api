from fastapi import FastAPI
from app.routers import users, projects

app = FastAPI()

app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(projects.router, prefix="/projects", tags=["projects"])

@app.get("/")
def read_root():
    return {"message": "TaskFlow API", "version": "0.1.0"}