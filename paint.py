

# goal: to find minimum cost of cans to paint wall


#ASSUMPTIONS

#choose one brand of paint cans
#choose paint from only one website
#choose only one colour (for now)
#wall is rectangular
#that paint cans come in distinct sizes 
#on average litre of paints covers on average 6.5 metres


# a dict containing the sizes of paint cans and how many litres of paint they can hold


paint_sizes= {"Half Pint": 0.24,
                "Pint": 0.47, 
                'Quart': 0.95,
                "Half Gallon": 1.89,
                "Gallon": 3.79,
                "5 Gallon": 18.93}



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

    total_litres = surface_area/6.5
    return total_litres


def sort_sizes(dict: dict, litres: float) -> list:
    
    """Returns a list of keys and values from a dic. It inserts the value of 'liters'
    in the list of values, and returns the new list of values sorted in asceding order"""
    
    #first put the values of all the available cans in a list:
    val_list = list(dict.values())
    key_list = list(dict.keys())
    #then append the number of litres we have in this list and sort it in ascending order
    val_list.append(litres)
    val_list = sorted(val_list)

    return key_list, val_list



#if it is cheaper to get the next size up,
#key_list, val_list = sort_sizes(paint_sizes, total_litres)
#index = val_list.index(total_litres)
#for paint_can, total_litres in paint_sizes.items():
 #           needed_cans[key_list[can_size]] += can
  #          val_list.remove(total_litres)

#and get the key paint can sizes dictionary by value
#can_size = val_list.index(index + 1)
#key_list[can_size]

def get_cans(total_litres: float) -> dict:

    """ A function that returns the number of cans needed to paint a wall in a dict"""

    # a list that will give us the total set  of cans we need to paint a wall
    needed_cans = {}

    #consider edge cases first. Litres needed is less than smallest can.
    if total_litres < paint_sizes["Quart"]:
        needed_cans.get("Quart", default=1)

    #assume that the paint needed happens to be exactly the one in the dict
    for paint_can, total_litres in paint_sizes.items():
        if total_litres in paint_sizes.items():
            needed_cans.get(needed_cans[paint_can], default=1)

    #assume that paint needed is more than 5 gallons:
    if total_litres > 18.93:
        #find out how many large paint cans we need:
        large_paint_cans_needed = total_litres//18.93
        needed_cans['5 Gallon'] += large_paint_cans_needed

        #subtract paint that was covered from the large paint cans from total beginning paint
        total_litres =- total_litres * 18.93
        if total_litres ==0:
            return needed_cans
        #call function recursively here
        get_cans(total_litres)

    #main case: litres of paint needed is a volume in between the sizes displayed.

    if total_litres not in paint_sizes.values() and total_litres < 18.93:
        #apply sorting function
        key_list, val_list = sort_sizes(paint_sizes, total_litres)

        #finally divide the number of total litres by the the paint can volumeimmediately preceding it
        #this assuming that this is the cheaper way to do it. Could be cheaper getting more paint dependingon the margin
        index = val_list.index(total_litres)

        #and get the key paint can sizes dictionary by value
        can_size = val_list.index(index-1)
        can = total_litres / val_list[index]
        key_list[can_size]
        
        for paint_can, total_litres in paint_sizes.items():
            needed_cans[key_list[can_size]] += can
            val_list.remove(total_litres)

        if total_litres == 0:
            val_list.remove(total_litres)
            return needed_cans
        
        get_cans(total_litres)

        

    return needed_cans


