# importing modules from converter
# import converter
#
# ans = converter.lbs_to_kg(10)
# print(ans)
# another way of importing functions instead of .

from converter import kg_to_lbs

ans = kg_to_lbs(100)
print(ans)

from utils import find_max
array_of_nums = []
n = int(input("Enter the length of list: "))
for i in range(0, n):
    element = int(input())
    array_of_nums.append(element)
# array_of_nums = [1, 2, 3, 4, 57, 8, 9, 6, 4, 5, 6, 7]
ans = find_max(array_of_nums)
print(ans)