# numbers = [1,2,3]
# ma tran (mang 2 chieu):
#  [1, 2, 3]
#  [4, 5, 6]
#  [7, 8, 9]
matrix = [
    [1 ,2 ,3],
    [4, 5, 6],
    [7, 8 ,9]
]
#print (matrix[1][1]) # cac so bat dau tu so 0 nen print in ra 5
#print (matrix[1][2]) # so 6 ([doc][ngang])
for row in matrix:
    for column in row:
        print(column)