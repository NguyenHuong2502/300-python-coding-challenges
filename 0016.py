# viết hàm để kiểm tra một chuỗi có phải là palindrome không 
def is_palindrome(s):
    s = ''.join(char.lower() for char in s if char.isalnum())
    return s == s[::-1]
input_string = input("Nhập một chuỗi:")
if is_palindrome(input_string):
    print (f'"{input_string}" là palindrome')
else :
    print (f'"{input_string}" không phải là palindrome')
