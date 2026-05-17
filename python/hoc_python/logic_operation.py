# Toán tử logic 
# AND cả hai đều đúng thì mới trả về giá trị
# OR một trong hai đúng sẽ trả về giá trị đúng,một trong hai sai thì trả về sai

a = 200
b = 50
c = 100
d = 100
e = 200
n = 50
if (a > b) and (a > c):
    print("a là số lớn nhất")
if (n == b) or (n == c):
    print("có ít nhất một trong số bằng giá trị với n")
if not d > b:
    print("d không lớn hơn b")