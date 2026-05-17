number = 2
text = 'python'
my_age = 20
my_wife_age = 18
text_2= 'my age is {0} and my wife age is {1}'   # Sử dụng dấu ngoặc nhọn {} để đánh dấu vị trí chèn giá trị, số trong ngoặc chỉ định thứ tự của các đối số được truyền vào phương thức format()

print(str(number) + " " + text)                  # Sử dụng phép cộng chuỗi (string concatenation)

print(text.format(number))                       # Sử dụng phương thức format để chèn giá trị vào chuỗi
print(text_2.format(my_age,my_wife_age))         # Sử dụng phương thức format để chèn nhiều giá trị vào chuỗi
