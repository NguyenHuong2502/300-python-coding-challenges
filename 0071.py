# OPEN FILE
file = open("test.txt")
print(file.read())
# write a content in the file
content = "huong dang tap code"
path = "test.txt"
with open(path ,"w") as file:
    print(file.write(content))