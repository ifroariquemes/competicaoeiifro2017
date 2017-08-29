n = int(input())
l = [int(x) for x in input().split(" ") if x]

menor = min(l)
posicao = l.index(menor)

print("Menor valor: %d" % menor)
print("Posicao: %d" % posicao)