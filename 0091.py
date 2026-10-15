# viet chuong trinh bat loi chia cho khong
try:
    n = int(input("nhap vao 1 so n"))
    result = n/ 0 
except ZeroDivisionError:
    result =    "Error: Division by zero is not allowed ! "
print(result)
