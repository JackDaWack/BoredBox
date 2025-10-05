from fastapi import FastAPI
from games.randomizer import get_random_game
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins; restrict in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Hello, world! I am bored."}

@app.get("/random-game")
def random_game():
    game = get_random_game()
    return {"game": game}

@app.get("/activities")
def get_activities():
    activities = [
        {"id": 1, "name": "Read a book"},
        {"id": 2, "name": "Go for a walk"},
        {"id": 3, "name": "Play a board game"}
    ]
    return activities
