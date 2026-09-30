# viết chương trình xóa 1 phần tử khỏi danh sách 
def xoa_phantu(danhsach, x):
    danhsach.remove(x)
    return danhsach

danhsach = [1, 2, 4, 5]

x = int(input("Nhap phan tu can xoa: "))

result = xoa_phantu(danhsach, x)

print(result)
