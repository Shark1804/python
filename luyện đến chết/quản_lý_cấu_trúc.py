class Ma_sinh_vien:
    def __init__(self,diem_toan,diem_ly,diem_tin,ma_sv,ho_ten):  #phương thức khởi tạo để tạo một đối tượng sinh viên mới với các thuộc tính điểm toán, điểm lý, điểm tin học, mã sinh viên và họ tên
        self.diem_toan = diem_toan                                   #gán giá trị điểm toán cho thuộc tính diem_toan của đối tượng sinh viên
        self.diem_ly = diem_ly                                       #gán giá trị điểm lý cho thuộc tính diem_ly của đối tượng sinh viên
        self.diem_tin = diem_tin                                     #gán giá trị điểm tin học cho thuộc tính diem_tin của đối tượng sinh viên
        self.ma_sv = ma_sv                                           #gán giá trị mã sinh viên cho thuộc tính ma_sv của đối tượng sinh viên
        self.ho_ten = ho_ten                                         #gán giá trị họ tên cho thuộc tính ho_ten của đối tượng sinh viên

    def diem_trung_binh(self):             # Tính điểm trung bình
        return (self.diem_toan + self.diem_ly + self.diem_tin) / 3   #tính điểm trung bình bằng cách cộng điểm toán, lý và tin học lại với nhau rồi chia cho 3
    
    def hien_thi(self):                    #hiển thị thông tin sinh viên
        print(f"SV{self.ma_sv} | {self.ho_ten} | Toán {self.diem_toan:.1f} | lý {self.diem_ly:.1f} | Tin {self.diem_tin:.1f} | ĐTB {self.diem_trung_binh():.2f}")    #.1f là in ra 1 chữ số thập phân sau dấu phẩy,.2f là in ra 2 chữ số thập phân sau dấu phẩy

    def xep_loai(self):                    # Xếp loại học bổng
        dtb = self.diem_trung_binh()                                 #tính điểm trung bình của sinh viên bằng cách gọi phương thức diem_trung_binh() và lưu kết quả vào biến dtb
        if dtb >= 8:                                                 #nếu điểm trung bình lớn hơn hoặc bằng 8 thì sinh viên đạt học bổng, phương thức sẽ trả về chuỗi "đạt học bổng"
            return "đạt học bổng"
        else:
            return "không đạt học bổng"
        

#----------nhập dữ liệu----------
danh_sach_sv = []
try:
    n = int(input("nhập số lượng sinh viên: "))                        #yêu cầu người dùng nhập số lượng sinh viên và chuyển đổi sang kiểu int, nếu người dùng nhập một giá trị không phải là số nguyên
except ValueError:
    print("vui lòng nhập một số nguyên hợp lệ.")                       #nếu người dùng nhập một giá trị không phải là số nguyên, sẽ in ra thông báo lỗi và đặt n thành 0 để không có sinh viên nào được nhập
    n = 0

for i in range (n):
    try:
        print(f"nhập mã sinh viên {i+1}:")                              #in ra thông báo yêu cầu người dùng nhập mã sinh viên thứ i+1 (vì i bắt đầu từ 0 nên cần cộng thêm 1 để hiển thị đúng số thứ tự)
        ma_sv = input("nhap ma sv:")                                    #nhập mã sinh viên từ người dùng và lưu vào biến ma_sv
        ho_ten = input("nhap ho ten:")                                  #nhập họ tên sinh viên từ người dùng và lưu vào biến ho_ten
        diem_toan = float(input("nhap diem toan:"))                     #nhập điểm toán từ người dùng, chuyển đổi sang kiểu float và lưu vào biến diem_toan
        diem_ly = float(input('nhap diem ly:'))                         #nhập điểm lý từ người dùng, chuyển đổi sang kiểu float và lưu vào biến diem_ly
        diem_tin = float(input('nhap diem tin:'))                       #nhập điểm tin học từ người dùng, chuyển đổi sang kiểu float và lưu vào biến diem_tin
    except  ValueError:
        print("vui lòng nhập một số hợp lệ cho điểm.")                  #nếu người dùng nhập một giá trị không phải là số cho điểm, sẽ in ra thông báo lỗi và bỏ qua sinh viên đó
        continue

sv = Ma_sinh_vien(diem_toan,diem_ly,diem_tin,ma_sv,ho_ten)              #tạo một đối tượng sinh viên mới với thông tin đã nhập
danh_sach_sv.append(sv)                                                 #thêm đối tượng sinh viên mới vào danh sách sinh viên

#----------in danh sach sinh viên----------
print("\n danh sach sinh vien")
for sv in danh_sach_sv:                                                 #lap qua tung sinh vien trong danh sach sinh vien
    sv.hien_thi()                                                       #goi ham hien thi de in ra thong tin cua tung sinh vien

#----------hoc bổng----------
print("\n danh sach sinh vien đạt học bổng")                            
for sv in danh_sach_sv:                                                 #lap qua tung sinh vien trong danh sach sinh vien
    if sv.xep_loai() == "dạt học bổng":                                 #goi ham xep loai de kiem tra xem sinh vien co dat hoc bong hay khong
        sv.hien_thi()                                                   #neu sinh vien dat hoc bong thi goi ham hien thi de in ra thong tin cua sinh vien do

#----------xep loai giam dan theo diem trung binh----------
danh_sach_sv.sort(key=lambda sv: sv.diem_trung_binh(),reverse = True)   #vs moi sinh vien lay diem trung binh ra de so sanh
#lambda la 1 ham an danh, chi su dung 1 lan, khong can dat ten, sau do goi ham do trong sort

print("\n danh sach sinh vien xep loai giam dan theo diem trung binh")  #in ra danh sách sinh viên đã được sắp xếp theo điểm trung bình giảm dần
for sv in danh_sach_sv:                                                 #lap qua tung sinh vien trong danh sach sinh vien da duoc sap xep
    sv.hien_thi()                                                       #goi ham hien thi de in ra thong tin cua tung sinh vien