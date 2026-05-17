# Dictionary - Từ điển
#   Key    |   Value
# +--------------------+
# | hello  |   xin chào|
# +--------------------+

english_vietnamese_dictionary = {
    "hello" : "xin chào",
    "goodbye": "tạm biệt",
    "morning":"buổi sáng",
    "tea": "trà",
    "milk":"sữa"
}

print(english_vietnamese_dictionary["hello"])
print(english_vietnamese_dictionary.get("cat","từ khóa này không tồn tại"))    #in ra nghĩa trong từ điển (dictionary) "từ cần tìm nghĩa", "lệnh in ra nếu không thể tìm thấy nghĩa của từ đó"(chỉ có get ms làm đc)