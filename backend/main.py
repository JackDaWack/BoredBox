from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, world! I am bored."}

@app.get("/activities")
def get_activities():
    activities = [
        {"id": 1, "name": "Read a book"},
        {"id": 2, "name": "Go for a walk"},
        {"id": 3, "name": "Play a board game"}
    ]
    return activities    
