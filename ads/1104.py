n = input().split(" ")

while n[0] != '0' and n[1] != '0':
    ana = set([int(x) for x in input().split()])
    beatriz = set([int(x) for x in input().split()])

    diff = min(len(ana - beatriz), len(beatriz - ana))
    print(diff)

    n = input().split(" ")
