# viet ham de tinh tong cac so tu 1 den n 
def tong(n):
    tong = 0 
    for i in range (1,n+1): 
        tong = tong + i 
    return tong 
n = int(input('nhap vao so n'))
result = tong(n)
print (result)