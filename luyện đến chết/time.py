# Bài 150 : cho log truy cập :timestamp (time dạng HH:MM)
# Yêu cầu : tìm khoảng 1 giờ (vd : 14:00 - 14:59) có nhiều truy cập nhất

n = int(input("Nhập số lượng log truy cập: "))           #nhập số lượng log truy cập
dem = {}                                                 #tạo một dictionary để đếm số lần truy cập cho mỗi giờ
for _ in range(n):                                       #lặp qua từng log truy cập
    tg = input('nhập thời gian truy cập: ').strip()      #nhập thời gian truy cập và loại bỏ khoảng trắng
gio = tg [:2]                                            #lấy phần giờ từ thời gian truy cập (2 ký tự đầu tiên)
dem[gio] = dem.get(gio,0) +1                             #cập nhật số lần truy cập cho giờ đó trong dictionary, nếu chưa có thì khởi tạo là 0 và cộng thêm 1

max_gio = None                                           #biến để lưu giờ có nhiều truy cập nhất
max_lan = 0                                              #biến để lưu số lần truy cập nhiều nhất

for gio in dem:                                          #lặp qua từng giờ trong dictionary
    if dem[gio] > max_lan:                               #nếu số lần truy cập của giờ hiện tại lớn hơn số lần truy cập nhiều nhất đã lưu
        max_lan = dem[gio]                               #cập nhật số lần truy cập nhiều nhất
        max_gio = gio                                    #cập nhật giờ có nhiều truy cập nhất

print(f'khoảng thời gian có nhiều truy cập nhất là: {max_gio}:00 - {max_gio}:59 với {max_lan} truy cập') #in ra khoảng thời gian có nhiều truy cập nhất và số lần truy cập trong khoảng đó