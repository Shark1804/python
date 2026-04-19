# ứng dụng máy tính cơ bản
num1 = float(input('Nhập vào số thứ nhất: '))
num2 = float(input('Nhập số thứ hai: '))
operator = input("nhập vào toán tử: ")

if (operator == "+"):
    print(f"num1 + num2 = {num1 + num2}")
elif (operator == "-"):
    print(f"num1 - num2 = {num1 - num2}")
elif (operator == "*"):
    print(f"num1 * num2 = {num1 * num2}")
else:
    print("toán tử không hợp lệ!!")