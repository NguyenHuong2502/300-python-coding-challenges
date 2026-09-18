# viết hàm tính giai thừa của 1 số 
def giai_thua(n):
    if n <= 0 : 
        return "vui long nhap so lon hon 0"
    result = 1
    for i  in range (1,n+1):
        result = result * i 
    return result
try : 
    n = int(input("nhap vao so tu nhien n"))
    result = giai_thua(n)
    print(result)
except : 
    print ("vui lonng nhap so")