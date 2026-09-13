# write a program that checks a value is even or odd
def check_even_odd():
    value = int(input('enter a value: '))
    if value % 2 == 0 : 
        return "value is even"
    else : 
        return "value is odd"   

result = check_even_odd()   
print(result)

