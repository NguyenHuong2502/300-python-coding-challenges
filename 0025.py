# viét chương trình đếm số lần xuất hiện của một phần tử trong danh sách 
def count_phantu(danhsach,x):
    count = 0 
    for i in danhsach:
        if i == x : 
            count += 1 
    return count 
x = int(input("nhap vao phan tu x"))
danhsach = [2,5,7,8,8,9,2]
result = count_phantu(danhsach,x)
print(result) # co the dung ham count co san cua python 