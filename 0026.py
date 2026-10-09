# Tao mot dictionary
my_dict = {}
my_dict ['name'] = "Huong"
my_dict['age'] = 22
print (my_dict)

# truy cap gia tri cua mot key trong dict
print (my_dict['name'])
print(my_dict.get("name"))

# xoa mot cap key-value khỏi danh sach
key_to_delete = input("nhap tu can xoa")
if key_to_delete in my_dict:
    my_dict.pop(key_to_delete)
    print(f"da xoa{key_to_delete}")
    print(my_dict)
else :
    print(f"khong ton tai {key_to_delete}")

