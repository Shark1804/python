# tuple là một kiểu dữ liệu không thể thay đổi (immutable) trong Python, 
# được sử dụng để lưu trữ một tập hợp các giá trị. Các giá trị trong tuple có thể là bất kỳ kiểu dữ liệu nào, 
# và chúng được phân tách bằng dấu phẩy. Một tuple có thể chứa nhiều phần tử, 
# và chúng được đặt trong dấu ngoặc đơn ().
coordinates = (123,456)
#               0   1
# nếu gắn tiếp giá trị cho tuple thì chương trình sẽ báo lỗi
coordinates2= [(1,2),(3,4),(5,6)]
#                0     1     2
print(coordinates[0])             #in ra phần tử thứ 0 của tuple coordinates
print(coordinates2[1])            #in ra phần tử thứ 2 của tuple trong list coordinates2
print(coordinates2[1][0])         #in ra phần tử thứ 0 của