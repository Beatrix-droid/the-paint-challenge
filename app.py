from flask import Flask, render_template, request
from paint import get_surface_area

app = Flask(__name__)
@app.route('/')
def hello_world():
    if request.method == "POST":
        pass

    return render_template("index.html")



if __name__ == "__app__":
    app.run()