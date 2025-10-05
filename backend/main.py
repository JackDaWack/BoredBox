from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, world!"}

@app.route('/activities', methods=['GET'])
def get_activities():
    activities = [
        {"id": 1, "name": "Read a book"},
        {"id": 2, "name": "Go for a walk"},
        {"id": 3, "name": "Play a board game"}
    ]
    return jsonify(activities)

if __name__ == '__main__':
    app.run(debug=True)