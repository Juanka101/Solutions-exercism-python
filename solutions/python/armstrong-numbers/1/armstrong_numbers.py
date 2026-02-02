def is_armstrong_number(number):
    count = 0
    operations_number = number
    while operations_number > 0:
        digit = operations_number % 10
        print(digit)
        count +=  (digit ** len(str(number)))
        operations_number =  operations_number // 10
        
    if number == count:
        return True
    else:
        return False