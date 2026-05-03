import math

def is_prime(num):
    if num > 1:
        for i in range(2, int(num / 2)):
            if (num % i) == 0:
                print("False")
                break
        else:
            print("True")
    elif num == 4:
        print("False")
    else:
        print("True")



num = int(input())
is_prime(num)