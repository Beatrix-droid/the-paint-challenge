from flask import Flask, render_template, request, flash
from paint import get_surface_area

app = Flask(__name__)
app.secret_key = '_5#y2L"F4Q8z\n\xec]/'


@app.route('/', methods=["POST", "GET"])
def hello_world():
    if request.method == "POST":
        width = float(request.form["width"])
        length = float(request.form["length"])
        area = get_surface_area(width, length)
        flash(area)
    return render_template("index.html")



if __name__ == "__app__":
    app.run()