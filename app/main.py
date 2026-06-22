from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "TaskFlow API", "version": "0.1.0"}