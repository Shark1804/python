# B1:Two sum
#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#You may assume that each input would have exactly one solution, and you may not use the same element twice.
#You can return the answer in any order.

#Cho một mảng các số nguyên nums và một số nguyên target, hãy trả về chỉ số của hai số đó sao cho tổng của chúng bằng target.
#Bạn có thể giả định rằng mỗi đầu vào chỉ có duy nhất một lời giải, và bạn không được sử dụng cùng một phần tử hai lần.
#Bạn có thể trả về câu trả lời theo bất kỳ thứ tự nào.

nums = list(map(int,input('nhap mang: ').split()))
target = int(input('nhap target: '))
class Solution:                                             #tao class Solution(lop) de giai quyet bai toan
    def twoSum(self,sums,target):                           #self:chinh object,sums: mang so nguyen, target: so nguyen can tim
        for i in range(len(sums)):                          #duyet qua tung phan tu trong mang sums i la index cua phan tu
            for j in range(i+1,len(sums)):                  #lap tiep de tim phan tu thu 2,i+1 de tranh lap lai chinh no(khong bi trung voi i)
                if sums[i] + sums[j] ==target:              #kiem tra neu tong cua 2 phan tu co bang target khong
                    return [i,j]                            #neu bang thi tra ve chi so cua 2 phan tu do