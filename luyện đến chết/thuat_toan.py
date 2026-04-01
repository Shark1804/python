# Bài 19 : cho một mảng số nguyên gồm n phần tử và một số nguyên k
# Hãy tìm tất cả các phần tử của mảng mà có giá trị lớn nhất nhưng không vượt quá k
# Yêu cầu giải thuật có độ phức tạp O(n log n) hoặc tốt hơn

k= int(input('nhập K: '))
integer_list = list(map(int, input('nhập mảng: ').split()))
n= int(input('nhập số phần tử n: '))

#sắp xếp mảng
integer_list.sort()

left = 0                                                     #con trỏ trái bắt đầu từ đầu mảng
n = len(integer_list)                                        #đếm độ dài của mảng từ phần tử n 
right = n - 1                                                #con trỏ phải bắt đầu từ cuối mảng

tong_tot_nhat = -1                                           #khởi tạo tổng tốt nhất ban đầu là -1
cap_tot_nhat = None                                          #khởi tạo cặp tốt nhất ban đầu là None

while left < right:                                          #duyệt khi 2 con trỏ chưa gặp nhau
    tong = integer_list[left] + integer_list[right]          #tính tổng của cặp hiện tại

    if tong > k:                                             #nêu tổng vượt quá K
        right -= 1                                           #thu hẹp pham vi bằng cách di chuyển con trỏ phải sang trái
    else:                                                    #nếu tổng không vượt quá k (thỏa mãn điều kiện)
        if tong > tong_tot_nhat:                             #nếu tổng của cặp hiện tại lớn hơn tổng tốt nhất đã tìm được
            tong_tot_nhat = tong                             #cập nhật tổng tốt nhất
            cap_tot_nhat = (integer_list[left], integer_list[right]) #cập nhật cặp tốt nhất
        left += 1                                            #di chuyển con trỏ trái sang phải để tìm cặp có tổng lớn hơn

# in kết quả
print('\n====KẾT QUẢ====' )
if cap_tot_nhat:
    print('cặp thỏa mãn tốt nhất:',cap_tot_nhat)
    print('tổng :',tong_tot_nhat)
else:
    print('không tìm thấy cặp nào')