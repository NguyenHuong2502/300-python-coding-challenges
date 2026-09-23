# viết chương trình để tạo danh sách các số từ 1 đến 100
list = []
def print_list(n):
    for i in range(1, n+1) : 
        list.append(i)
    return list
n = int(input('nhập vào số n'))
print (print_list(n))