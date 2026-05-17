student_name = ["John Doe", "Jane Smith", "Alice Johnson", "Bob Brown"]
math_scores = [85, 92, 78, 90]
#student_name.extend([math_scores])                 # Thêm danh sách điểm số vào danh sách tên sinh viên
student_name.append("Charlie Davis")                # Thêm một tên sinh viên mới vào cuối danh sách
student_name.insert(1, "Emily Wilson")              # Chèn một tên sinh viên mới vào vị trí index 1


#student_name.clear()                               # Xóa tất cả phần tử trong danh sách
#student_name.pop()                                 # Xóa phần tử cuối cùng trong danh sách
#student_name.remove("Alice Johnson")               # Xóa phần tử có giá trị "Alice Johnson" khỏi danh sách
#print(student_name.index("Bob Brown"))             # tìm phần tử "Bob Brown" trong danh sách va trả về index của nó
#print(student_name.count("John Doe"))              # đếm số lần xuất hiện của phần tử "John Doe" trong danh sách
#student_name.sort()                                # Sắp xếp danh sách tên sinh viên theo thứ tự chữ cái tăng dần
#math_scores.sort()                                 # Sắp xếp danh sách điểm số theo thứ tự tăng dần
#math_scores.reverse()                              # Đảo ngược thứ tự của danh sách điểm số
student_name2 = student_name.copy()                 # coppy toàn bộ list của student_name                        # Tạo một bản sao của danh sách tên sinh viên
print("Student Names:", student_name)
print("Math Scores:", math_scores)
print('student name 2 : ',student_name2)
