#trò chơi đoán từ
secret_word = "python"
hint = "gợi ý: đây là tên một ngôn ngữ lập trình"
guess = ""
guess_count = 0
guess_limit = 3

print(hint)                                         #in ra gợi ý
while guess !=  secret_word:                        #nếu từ đoán khác kết quả thì tiếp tục in câu hỏi
    if guess_count < guess_limit:                   #nếu lượt đoán nhỏ hơn lượt giới hạn thì chạy lệnh ở dưới , nếu không thì chạy lệnh else
        guess = input("bạn đoán đây là từ gì? ")    #đoán từ 
        guess_count += 1                            # mỗi lần đoán cộng count lên 1 lần
    else:                                           # nếu thỏa mãn else break dòng lệnh và ngay lập tức chạy lệnh dưới
        break                                       # dừng dòng lệnh

if secret_word == guess:                            # nếu đoán đúng thì in ra đúng
    print("bạn đã đoán chính sác") 
else:                                               # thỏa mãn else ở trên sẽ chạy lệnh dưới
    print('bạn đã thất bại vì đoán sai quá 3 lần')