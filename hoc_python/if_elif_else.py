a = 50
b = 100
if a > b:                  #nếu điều kiện a > b đúng thì sẽ thực hiện khối mã bên dưới
    print("a lớn hơn b")   #nếu điều kiện a > b sai thì sẽ bỏ qua khối mã bên trên và kiểm tra điều kiện elif
elif a < b:                #nếu điều kiện a < b đúng thì sẽ thực hiện khối mã bên dưới
    print('a nhỏ hơn b')   #nếu điều kiện a < b sai thì sẽ bỏ qua khối mã bên trên và kiểm tra điều kiện else
else:                      #nếu điều kiện a > b và a < b đều sai thì sẽ thực hiện khối mã bên dưới
    print('a bằng b')      #nếu điều kiện a > b và a < b đều sai thì sẽ thực hiện khối mã bên trên