from flask import Flask, render_template, request

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
    return render_template("home.html", movies=movies)

@app.route("/new_movie", methods=["GET", "POST"])
def new_movie():
    error = ""
    success = ""

    form_data = {
        "title": "",
        "genre": "",
        "director": "",
        "year": ""
    }

    if request.method == "POST":
        title = request.form.get("title", "").strip()
        genre = request.form.get("genre", "").strip()
        director = request.form.get("director", "").strip()
        year = request.form.get("year", "").strip()

        form_data["title"] = title
        form_data["genre"] = genre
        form_data["director"] = director
        form_data["year"] = year

        if title == "":
            error = "Title is required."
        elif len(title) > 100:
            error = "Title must be 100 characters or less."
        elif genre == "":
            error = "Genre is required."
        elif len(genre) > 50:
            error = "Genre must be 50 characters or less."
        elif director == "":
            error = "Director is required."
        elif len(director) > 100:
            error = "Director must be 100 characters or less."
        elif year == "":
            error = "Year is required."
        elif not year.isdigit():
            error = "Year must be a number."
        elif int(year) < 1888 or int(year) > 2100:
            error = "Year must be between 1888 and 2100."
        else:
            success = "Form input looks good."

    return render_template("new_movie.html", error=error, success=success, form_data=form_data)

if __name__ == "__main__":
    app.run(debug=True)