from array import array
from curses.ascii import isprint
from itertools import count
from operator import index

# #Subscripting
# print("Hello"[0])
#
# #Integer
# print(12334556)
#
# #Float
# print(3.14156)
#
# #Boolean
# print(True)
def twoSum(nums,target):
    k = {}
    for i in range(0, len(nums)):
        p1 = nums[i]
        p2 = target - p1
        if p1 in k.keys():
            return (i, k[p1])
`        else:
            k[p2] = i
    return None


nums = [int(x) for x in input().split()]
target = int(input())
print(twoSum(nums,target))





