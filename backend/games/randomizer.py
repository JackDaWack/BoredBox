import random

def get_random_game():
    games = [
        "hangman",
        "fighting",
        "reaction"
    ]
    return random.choice(games)