#viet chuong trinh de tao mot chuoi
string = "hello huynh huong"
print(string)
#viet chuong trinh de noi hai chuoi
string2 = "co gang hoc nha"
print(string + string2)
str3 = ''.join([string,string2])
print(str3)
str1 = 'huong'
str4 = 'xinh'
chuoi = f"{str1}{str4}"
print(chuoi)
Chuoi = "{}{}".format(str1,str4)
print(Chuoi)
print(len(Chuoi))
length = 0 
for i in Chuoi:
    length += 1
print(length)

chuhoa = Chuoi.upper()
print(chuhoa)
