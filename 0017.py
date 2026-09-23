# viết hàm đảo ngược chuỗi 
def reverse_string(s): 
    s = s[::-3]
    return s 
text = input("Nhập chuỗi:")
result = reverse_string(text)
print(result)