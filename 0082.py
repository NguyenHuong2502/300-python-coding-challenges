# viet chuong trinh de ke thua tu mot lop co ban 
class Nguoi:
    def __init__(self,name, age):
        self.name = name
        self.age = age 
    def show_infor(self):
        print(f"Tên{self.name}")
        print(f"Tuổi:{self.age}")
class Hocsinh(Nguoi):
    def __init__(self,name,age, Class,avg_score):
        super().__init__(name,age)
        self.Class = Class
        self.avg_score = avg_score
    def show_infor(self):
        super().show_infor()
        print(f"Lớp:{self.Class}")
        print(f"Điểm trung bình:{self.avg_score}")
    def rank(self):
        if self.avg_score >= 9 : 
            return "Giỏi"
        else : 
            return "Dưới Giỏi"
hs = Hocsinh('Nguyễn Huỳnh Hương',22,"12A3",7)
print(hs.rank())
hs.show_infor()