# viet chuong trinh de in tat ca cac so nguyen tu 1 den 100
danhsach = []
def so_nguyen_to(n):

    if n < 2:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True
def in_danh_sach():
    for i in range (1,100):
        if so_nguyen_to(i):
            print (i) 

result = in_danh_sach()
print (result) 