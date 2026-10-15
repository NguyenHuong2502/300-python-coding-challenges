# viet chuong trinh bao loi khi truy cap key khong ton tai trong dictionary
try:
    my_dict = {'name':'Hương','age':22}
    result = my_dict['adress']
except KeyError:
    result = "ERROR: key khong ton tai trong tu dien"
print(result)
