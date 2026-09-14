def print_multiplication_table():
    for j in range(2, 10):
        print("Bảng cửu chương", j)

        for i in range(1, 11):
            result = j * i
            print(j, "x", i, "=", result)

        print()


print_multiplication_table()
