def value(colors):
    
    dict = { "black" : 0,
             "brown" : 1,
             "red" : 2,
             "orange" : 3,
             "yellow" : 4,
             "green" : 5,
             "blue" : 6,
             "violet" : 7,
             "grey" : 8,
             "white" : 9,}
    
    color_one = dict[colors[0]]
    color_two = dict[colors[1]]
    
    return int(str(color_one) + str(color_two))