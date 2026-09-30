# viet chuong trinh them mot phan tu vao dau danh sach 
def them_dau(danhsach,x):
    danhsach.insert(0,x)
    return danhsach
danhsach = [3,6,8,9]
x = int(input('nhap vao phan tu x'))
print (them_dau(danhsach,x))