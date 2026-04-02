teams = ['Team A', 'Team B', 'Team C', 'Team D']   #tao mot list chua ten cac doi bong (co the dung so hoac true/false)
      #     0          1         2          3
print(teams[0])
print(teams[1])
print(teams[2])
print(teams[3])    #in ra tung phan tu trong list theo index (index bat dau tu 0)
print(teams[-1])   #in ra phan tu cuoi cung cua list
#print(teams[...]) #in ra toan bo phan tu trong list
print(teams[1:3])  #in ra phan tu tu index 1 den index 2 (index 3 khong duoc in ra)
teams[1] = 'Team E'    #thay doi gia tri cua phan tu tai index 1
print(teams)         #in ra toan bo list sau khi thay doi
