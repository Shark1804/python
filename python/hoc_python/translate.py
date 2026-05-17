# ung dung bien doi ngon ngu
# bien doi cac chu cai co dau thanh khong dau
# á ắ à ạ ă ---> a
#vi du:
#    "Trần Minh Sáng" ---> "Tran Minh Sang"
#    "sáng và Ngân"   ---> "Sang va ngan"
def translate(text):
    translate = ""
    for character in text:
        if character.lower() in "áắàạă":
            if character.isupper():
                translate = translate + "A"
            else:
                translate = translate + "a"
        else:
            translate = translate + character
            # text = "sáng"
            # character = "S" --> translate = "" + "S" = "S"
            # character = "á" --> translate = "S" + "a"= "sa"
            #...
    return translate

text = input("nhap vao van ban ma ban muon dich: ")
print(translate(text))
