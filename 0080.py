# viet chương trinh de sao chep noi dung cua mot file sang file khac
file_path1  = "document.txt"
file_path2 = "destination.txt"
import os
with open(file_path1 , "r") as file : 
    content = file.read()
with open(file_path2 ,"w") as file :
    result = file.write(content)
print(result)
    
