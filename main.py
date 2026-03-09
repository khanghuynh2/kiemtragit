# main.py
# Chương trình tính tổng các số từ 1 đến n

# Nhập số n từ bàn phím
n = int(input("Nhập số n: "))
tong = 0
# Tính tổng từ 1 đến n
for i in range(1, n + 1):
    tong += i
# In kết quả
print("Tổng các số từ 1 đến", n, "là:", tong)