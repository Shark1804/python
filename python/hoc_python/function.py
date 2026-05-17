# Hàm là một khối mã có thể được tái sử dụng để thực hiện một nhiệm vụ cụ thể.
# Hàm có thể nhận đầu vào dưới dạng tham số và trả về một giá trị.
# Hàm được định nghĩa bằng cách sử dụng từ khóa def, theo sau là tên hàm và dấu ngoặc đơn chứa các tham số (nếu có). 
# Phần thân của hàm được thụt lề và chứa mã thực thi của hàm.
def say_hello(name,email):           # đặt gì cũng được nhưng khuyên nên dặt tên dúng với chức năng của nó
    print(f"Hello, {name}!")   # phần thân của hàm, có thể chứa nhiều dòng mã
    print(f"Email: {email}")

#print('bắt đầu chương trình')
#gọi hàm
say_hello('Alice','alice@gmail.com')             #gọi hàm say_hello với đối số 'Alice', sẽ in ra "Hello, Alice!"
say_hello('Bob','bob@gmail.com')               #gọi hàm say_hello với đối số 'Bob', sẽ in ra "Hello, Bob!"
say_hello('Charlie','charlie@gmail.com')           #gọi hàm say_hello với đối số 'Charlie', sẽ in ra "Hello, Charlie!"
#print('kết thúc chương trình')