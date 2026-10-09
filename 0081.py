# viết chương trình để tạo 1 lớp học sinh 
class Student :
    def __init__(self,name,code,age,score,adress):
        self.name  = name 
        self.code  = code 
        self.age = age
        self.score = score 
        self.adress = adress # thuọc tinh private 
    # hien thi thong tin hoc sinh
    def show_infor(self):
        print(f"Tên học sinh:{self.name}")
        print(f"Mã số học sinh : {self.code}")
        print(f"Tuổi học sinh:{self.age}")
        print(f"Điểm trung bình của học sinh:{self.score}")
        print(f"Địa chỉ của học sinh này là :{self.adress}")
    def ranking(self):
        if self.score >= 8.5:
            return "Giỏi"
        elif self.score >= 6.5:
            return "Khá"
        elif self.score >= 5.0:
            return "Trung Bình"
        else:
            return "Yếu"
    # cap nhap diem moi cho hoc sinh
    def update_score(self,new_score):
        self.score  = new_score
        print(f"Điểm mới cập nhật của học sinh là {self.score}")
    @property
    def age(self):
        return self.__age 
    @age.setter
    def age(self,new_age):
        if new_age > 0 :
            self.__age = new_age
        else :
            print("Tuổi không hợp lệ")

        

# tạo object
hs1 = Student('Nguyễn Huỳnh Hương',"3472",22,9,'THPHCM')
hs2 = Student('Võ Thị Kim Chi','3458',23,5,"QUY NHƠN")
# tao danh sach doi tuong hoc sinh 
danhsach = [hs1,hs2]
#print(hs1.show_infor())
#print(hs1.ranking())
#print(hs1.update_score(10))   
for hs in danhsach:
    hs.show_infor()

print(f"tuổi trước update:{hs2.age}")
hs.age = 78
print(hs.show_infor())