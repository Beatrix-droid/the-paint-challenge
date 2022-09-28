from flask import Flask, render_template, request, flash
from paint import get_surface_area, get_litres, get_cans, merge_dictionaries, paint_prices, get_price
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
        coat_number = float(request.form['coat_number'])
        
        #check if customer imputted any base options
        base_options = request.form["base_options"]
        if base_options == "yes":
            coat_number += 1
        #check if customer imputted any top options
        top_options = request.form["top_options"]
        if top_options == "yes":
            coat_number += 1

        area = coat_number*(get_surface_area(width, length) - get_surface_area(obstacle_width, obstacle_length))
        litres_needed = get_litres(area)
        cans_needed = get_cans(litres_needed)
        new_dict={key:((cans_needed[key])/2) for key in cans_needed}
        dict_3 = merge_dictionaries(new_dict, paint_prices)
        total_price = get_price(dict_3)
        new_dict["Total Price"] =f"{total_price}£"
        flash(new_dict)
    return render_template("index.html")



if __name__ == "__app__":
    app.run(debug=True)