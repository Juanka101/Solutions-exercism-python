def label(colors):
    
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

    count = 0
    cantidad_zero = dict[colors[2]]
    zeros = ""
    
    while count < cantidad_zero:
        count += 1
        zeros += "0"
    
    total_digit = str(color_one) + str(color_two) + zeros

    if total_digit[0] == "0" and total_digit[1] == "0":
        total_digit = 0 
    elif total_digit[0] == "0" and total_digit[1] != "0":
        total_digit = total_digit[1] + zeros

    if int(total_digit) >= 1000000000:
        return str(int(total_digit) // 1000000000) + " gigaohms"
    elif int(total_digit) >= 1000000:
        return str(int(total_digit) // 1000000) + " megaohms"
    elif int(total_digit) >= 1000:
        return str(int(total_digit) // 1000) + " kiloohms"
    else:
        return str(total_digit) + " ohms"


        
        
        
    