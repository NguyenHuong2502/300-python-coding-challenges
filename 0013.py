# viết hàm để kiểm tra 1 số có phải số nguyên tố không 
def KiemTra_Snt(n):
    if n < 2 : 
        return "Khong phai so nguyen to"
    for i in range(2,n):
        if n % i == 0 :
            return "khong phai so nguyen to"
    return "so nguyen to"
n = int(input("Nhap vao so nguyen n"))
result  = KiemTra_Snt(n)
print (result)
