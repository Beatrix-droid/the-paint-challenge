

# goal: to find minimum cost of cans to paint wall


#ASSUMPTIONS

#choose one brand of paint cans
#choose paint from only one website
#choose only one colour (for now)
#wall is rectangular
#that paint cans come in distinct sizes 
#on average litre of paints covers on average 6.5 metres


# a dict containing the sizes of paint cans and how many litres of paint they can hold

#average price of paint is 18.08£ and it was obtained by computing the average of the following list that
# contians a range of various Uk paints priced per litre
list = [13.99,13.49,15.99,8.00, 18.99,38.00 ]

#A dictionary of the most common paint tub sizes and there volume per litre was computed

paint_sizes= {"Half Pint": 0.24,
                "Pint": 0.47, 
                'Quart': 0.95,
                "Half Gallon": 1.89,
                "Gallon": 3.79,
                "5 Gallon": 18.93}

#using teh above dictionary and the average cost of paint in the uk, a list of average prices of paint per
#tub size was calculated

paint_prices={"Half Pint": 4.34,
                "Pint": 8.5, 
                'Quart': 17.18,
                "Half Gallon": 34.17,
                "Gallon": 68.52,
                "5 Gallon": 342.25}
                
#a dict that will hold all the tubs we need to paint a wall
needed_cans = {"Half Pint": 0,
                "Pint": 0, 
                'Quart': 0,
                "Half Gallon": 0,
                "Gallon": 0,
                "5 Gallon": 0}



#helper functions that will aid us in the main computation

def get_surface_area(height: float, width: float) -> float:

    """given the height and width
    (in metres) of a rectangular wall
    returns the suraface area
    """

    surface_area = height * width
    return surface_area


def get_litres(surface_area: float) -> float:

    """A function that accepts the surface area
    as a parameter and returns the number of litres used 
    to paint that surface area"""

    total_litres = surface_area/10
    return total_litres


def sort_sizes(dictionary: dict[str, float], litres: float) -> list:
    
    """Returns a list of values from a dic. It inserts the value of 'liters'
    in the list of values, and returns the new list of values sorted in asceding order"""
    
    #first put the values of all the available cans in a list:
    val_list = [dictionary[key] for key in dictionary]
    

    #then append the number of litres we have in this list and sort it in ascending order
    val_list.append(litres)
    val_list = sorted(val_list)

    return  val_list



def get_cans(total_litres: float) -> dict[str, float]:

    """ A function that accepts an integer representing
    litres of paint and returns the cheapest way of buying that many litres of paint according to the above 
    price listing"""

    
   
    #Case 1: Litres needed is less than smallest can.
    if total_litres < 0.47:
        small_cans= total_litres//0.24
        needed_cans["Half Pint"]+= small_cans
        total_litres =total_litres- small_cans*0.24

        if total_litres != 0:
        #call function recursively here
            needed_cans["Half Pint"]+= small_cans

        return needed_cans
    
    #Case 2: the ammount of litres needed happens to be exactly the dimensions of one tub
    for key, value in paint_sizes.items():
        if value == total_litres:
            needed_cans[key] += 1
            return needed_cans

    #Case3: the paint needed is more than 5 gallons:
    if total_litres > 18.93:
        #find out how many large paint cans we need:
        large_paint_cans_needed = total_litres//18.93
        needed_cans['5 Gallon'] = large_paint_cans_needed

        #subtract paint that was covered from the large paint cans from total beginning paint
        total_litres = total_litres - (18.93 * large_paint_cans_needed)
        
        if total_litres != 0:
        #call function recursively here
            get_cans(total_litres)
        return needed_cans

    #Case 4: litres of paint needed is a volume in between the sizes displayed.

    if (total_litres not in paint_sizes.values()) and (0.24 < total_litres < 18.93):
        #apply sorting function
        val_list = sort_sizes(paint_sizes, total_litres)

        #finally divide the number of total litres by the the paint can volumeimmediately preceding it
        #this assuming that this is the cheaper way to do it. Could be cheaper getting more paint dependingon the margin
        index_of_our_litres = val_list.index(total_litres)

        #and get the key paint can sizes dictionary by value
        can_size = val_list[index_of_our_litres-1]
        can_amount = total_litres // can_size
        for key, value in paint_sizes.items():
            if value == can_size:
                needed_cans[key] += can_amount
                val_list.remove(total_litres)
                #removing the litres covered by the can from the total litres remaining

                total_litres = total_litres - (can_amount*can_size) 
                if total_litres != 0:       
                    get_cans(total_litres)
                return needed_cans


def merge_dictionaries(dict_1: dict[str,float], dict_2:dict[str, float] ) -> dict[str, list]:
    
    """A function that accepts two dictionaries together, combining the value of each key value pair 
    in a list"""

    dict_3 = {**dict_1, **dict_2}
    for key, value in dict_3.items():
        if key in dict_1 and key in dict_2:
            dict_3[key] = [value , dict_1[key]]
    return dict_3


def get_price(dict_3: dict[str, list]) -> float:
    
    """A function that accepts a dictionary with lists of length two (containing 
    just integers) as as values pair"""
    prices_of_cans = []
    for value in dict_3.values():
        prices_of_cans.append(value[0]*value[1])
    total_price = sum(prices_of_cans)
    return total_price
