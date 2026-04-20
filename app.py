from flask import Flask

app = Flask(__name__)

movies = [
    {
        "id": 1,
        "title": "Interstellar",
        "genre": "Sci-Fi",
        "director": "Christopher Nolan",
        "year": 2014
    },
    {
        "id": 2,
        "title": "Spirited Away",
        "genre": "Animation",
        "director": "Hayao Miyazaki",
        "year": 2001
    }
]

@app.route("/")
@app.route("/home")
def home():
    return "Movie Watch List app is running."

if __name__ == "__main__":
    app.run(debug=True)