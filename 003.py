# write a program found the most bigest number in a list have 3 numbers
def find_biggest_number(n):
    biggest = numbers[0]
    for i in range(n):
        if numbers[i] > biggest:
            biggest = numbers[i]
    return biggest  
numbers = [5, 10, 3]
result = find_biggest_number(3)
print(result)

