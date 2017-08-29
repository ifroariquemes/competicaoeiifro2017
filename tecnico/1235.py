n = int(input())
for i in range(n):
    s = input()
    print (s[:len(s)//2][::-1] + s[len(s)//2:][::-1])