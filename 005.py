# viet chuong trinh de tinh diem trung binh và xep loại học sinh 
def caculate_average_score(diem):
    diemtb = sum(diem)/len(diem)
    return diemtb
try : 
    scores = []
    n = int(input("Nhập số lượng môn học: "))
    if n <= 0: 
        print("Số lượng môn học phải lớn hơn 0.")
    else:
        for i in range(n):
            score = float(input(f"Nhập điểm môn học thứ {i + 1}: "))
            if score < 0 or score > 10:
                print("Điểm phải nằm trong khoảng từ 0 đến 10.")
                break
            scores.append(score)
            if len(scores) == n:
                average_score = caculate_average_score(scores)
                print(f"Điểm trung bình: {average_score:.2f}")
                if average_score >= 9:
                    print("Xếp loại: Xuất sắc")
                elif average_score >= 8:
                    print("Xếp loại: Giỏi")
                elif average_score >= 7:
                    print("Xếp loại: Khá")
                elif average_score >= 5:
                    print("Xếp loại: Trung bình")
                else:
                    print("Xếp loại: Yếu")
except ValueError:
    print("Vui lòng nhập một số hợp lệ.")
               