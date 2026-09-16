# viet chương trình để đếm số lượng số chẵn và lẻ trong 1 danh sách 
def count_even_odd(n):
    count_even = 0 
    count_odd = 0 
    for i in n: 
        if i % 2 == 0 : 
            count_even += 1 
        else : 
            count_odd += 1 
    return count_even, count_odd
n = [2,6,7,9,11,10]
result = count_even_odd(n)
print (result)


