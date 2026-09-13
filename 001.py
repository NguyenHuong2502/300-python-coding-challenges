def check_value():
    value = int(input("enter a value:"))
    if value < 0 : 
        return "value is negative"
    else : 
        return "value is positive"

result = check_value()
print(result)