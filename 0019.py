# viet ham de tinh chi vi va dien tich hinh tron 
def chu_vi_va_dien_tich(r):
    chuvi  = 2 *3.14 *r 
    dientich = 3.14* r*r
    return chuvi, dientich
r =int(input("nhập vào bán kính r"))
result = chu_vi_va_dien_tich(r)
print (result)