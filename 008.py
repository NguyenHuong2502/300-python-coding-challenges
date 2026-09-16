# viet chương trinh kiem tra mot năm có phải năm nhuận không
def check_year(n):
    if n % 400 == 0 :
        return "năm nhuận"
    elif n % 4 == 0 and n % 100!=0: 
        return "năm nhuận"
    else:
        return "không phải năm nhuận"

n = int(input('nhập vào năm cần kiểm tra'))
result = check_year(n)

print (result)