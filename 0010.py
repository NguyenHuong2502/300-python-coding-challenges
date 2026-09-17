# viết chương trình để tìm ước chung lớn nhất của 2 số 
def UCLN(a,b):
    while b != 0 : 
        q = a // b
        r = a %b 
        print (a, "=", b ,"*",q,"+", r)
        a = b
        b = r
    return a 
result = UCLN(48,28
              )
print('UCLN', result)