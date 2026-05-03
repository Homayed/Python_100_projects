# print("Welcome to the Grand Band Generator\n")
# City = input("What city you grew up in?\n")
# Pet = input("What's your pet name\n")
# print("Your Band name should be " + City + " " + Pet)
from itertools import filterfalse
from re import split


# Python3 implementation
# to find unique digit
# numbers in a range

# Function to print
# unique digit numbers
# in range from l to r.
def printUnique(l, r):
    # Start traversing
    # the numbers
    list1 = []
    for i in range(l, r + 1):
        num = i
        visited = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        # Find digits and
        # maintain its hash
        while num:

            # if a digit occurs
            # more than 1 time
            # then break
            if visited[num % 10] == 1:
                break
            visited[num % 10] = 1
            num = (int)(num / 10)

        # num will be 0 only when
        # above loop doesn't get
        # break that means the
        # number is unique so
        # print it.
        if num == 0:
            list1.append(i)

    if list1[0]==l:
        print(list1[1])
    else:
        print(list1[0])



# Driver code
l = int(input())
r = 9999
printUnique(l, r)

















