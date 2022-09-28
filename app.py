from flask import Flask, render_template, request, flash
from paint import get_litres, get_cans, merge_dictionaries, paint_prices, get_price
import os
from dotenv import load_dotenv

app = Flask(__name__)

load_dotenv()
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")


@app.route('/', methods=["POST", "GET"])
def hello_world():
    if request.method == "POST":
        widths = request.form.getlist('width')
        lengths = request.form.getlist('length')
        obstacle_widths = request.form.getlist('obstacle_width')
        obstacle_lengths = request.form.getlist('obstacle_length')
        coat_number = float(request.form['coat_number'])
        
        #computing the areas of all the walls and summing them together
        wall_area = []
        for width, length in zip(widths, lengths):
            wall_area.append(float(width) * float(length))
        total_wall_area = sum(wall_area)

        obstacle_area = []
        for obstacle_width, obstacle_length in zip(obstacle_widths, obstacle_lengths):
            obstacle_area.append(float(obstacle_width) * float(obstacle_length))
        total_obstacle_area = sum(obstacle_area)


        #check if customer imputted any base options
        base_options = request.form["base_options"]
        if base_options == "yes":
            coat_number += 1
        #check if customer imputted any top options
        top_options = request.form["top_options"]
        if top_options == "yes":
            coat_number += 1

        
        
        area = coat_number*(total_wall_area - total_obstacle_area)
        if area <= 0:
            subtitle = {"Obstacle area can't be bigger than area to paint.": "Please make sure that you have entered the data correctly."}
            flash(subtitle)
            
        else:
            litres_needed = get_litres(area)
            cans_needed = get_cans(litres_needed)
            new_dict={key:((cans_needed[key])/2) for key in cans_needed}
            dict_3 = merge_dictionaries(new_dict, paint_prices)
            total_price = get_price(dict_3)
            new_dict["Total Price"] =f"{total_price}£"
            subt_title =  {'The number of different tubs needed and their price is':""}
            subt_title.update(new_dict)
            flash(subt_title)
    return render_template("index.html")



if __name__ == "__app__":
    app.run(debug=True)