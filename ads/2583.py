n = int(input())

for i in range(n):
    m = int(input())
    print("TOTAL")
    l = []
    for j in range(m):
        s = input().split(" ")
        if s[1] == "chirrin":
            l.append(s[0])
        elif s[1] == "chirrion":
            if s[0] in l:
                l.remove(s[0])
    for i in sorted(l):
        print(i)