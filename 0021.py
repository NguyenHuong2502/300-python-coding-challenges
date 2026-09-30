# viết chương trình để thêm 1 phần tử vào cuối danh sách 
def them_cuoi_ds(danhsach,x):
    danhsach.append(x)
    return danhsach
danhsach = [1,2,4,6,7]
x = int(input('nhap vao 1 phan tu'))
result = them_cuoi_ds(danhsach,x)
print(result)
