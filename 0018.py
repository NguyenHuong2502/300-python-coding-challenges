# viet ham tinh luy thua cua 1 so

def luy_thu(a,n):
    result = 1
    for i in range(n):
        result *= a 
    if n < 0 : 
        result = 1/ result 
    return result 
a = float(input("Nhập cơ số: "))
n = int(input("Nhập số mũ: "))
print (luy_thu(a,n))