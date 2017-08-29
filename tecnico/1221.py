import math
n = int(input())
for i in range(n):
    number = int(input())
    prime = True
    if n == 2 or n==3:
        print("Prime")
        break

    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            print("Not Prime")
            prime = False
            break
    if prime:
        print("Prime")