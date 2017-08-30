n = int(input())
for i in range(n):
    l = [int(x) for x in input().split(" ")]
    s = ''
    if l[2] == 0:
        s = "A porta fechou!"
    else:
        s = "A porta abriu!"
    print("%02d:%02d - %s" %(l[0],l[1],s))