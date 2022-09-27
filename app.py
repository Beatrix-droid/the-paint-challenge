from flask import Flask, render_template, request, flash
from paint import get_surface_area
import os
from dotenv import load_dotenv

app = Flask(__name__)

load_dotenv()
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")


@app.route('/', methods=["POST", "GET"])
def hello_world():
    if request.method == "POST":
        width = float(request.form["width"])
        length = float(request.form["length"])
        obstacle_width = float(request.form['obstacle_width'])
        obstacle_length = float(request.form['obstacle_length'])

        area = get_surface_area(width, length) - get_surface_area(obstacle_width, obstacle_length)
        flash(area)
    return render_template("index.html")



if __name__ == "__app__":
    app.run(debug=True)