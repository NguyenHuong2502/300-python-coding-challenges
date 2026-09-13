# viet chuong trinh tisnh tien taxi dua tren so km da di
def calculate_taxi_fare(km):
    fare = 0
    if km <= 1 :
        fare = km * 10.000
    elif 2 <= km <= 10:
        fare = 1 * 10.000 + (km - 1) * 8.000
    else:
        fare = 1 * 10.000 + 9 * 8.000 + (km - 10) * 6.000
    return fare

result = calculate_taxi_fare(12)
print(result)