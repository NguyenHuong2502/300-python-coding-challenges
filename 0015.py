# tính tổng các chử số của một số 
n = '234567'
def tinh_chu_so(n):
    tong = 0 
    for i in n: 
        tong += int(i)
    return tong 
result = tinh_chu_so(n)
print (result)

##

def sum_of_digits(n):
    n = abs (n)
    total  = 0 
    while n > 0 : 
        total += n % 10 
        n // 10 
    return total 
