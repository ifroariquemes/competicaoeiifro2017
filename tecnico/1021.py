valor = float(input())
notas100 = valor//100
valor = valor - notas100 * 100.0

notas50 = valor//50
valor = valor - notas50 * 50.0

notas20 = valor//20
valor = valor - notas20 * 20.0

notas10 = valor//10
valor = valor - notas10 * 10.0

notas5 = valor//5
valor = valor - notas5 * 5.0

notas2 = valor//2
valor = valor - notas2 * 2

moedas100 = valor//1
valor = valor - moedas100 * 1.0

valor = valor * 100
moeda50 = valor//50
valor = valor - moeda50 * 50

moeda25 = valor//25
valor = valor - moeda25 * 25

moeda10 = valor//10
valor = valor - moeda10 * 10

moeda5 = valor//5
valor = valor - moeda5 * 5

valor = round(valor) #evitar erros de precisão
moeda1 = valor//1
valor = valor - moeda1 * 1

print("NOTAS:")
print("%d nota(s) de R$ 100.00" % notas100)
print("%d nota(s) de R$ 50.00" % notas50)
print("%d nota(s) de R$ 20.00" % notas20)
print("%d nota(s) de R$ 10.00" % notas10)
print("%d nota(s) de R$ 5.00" % notas5)
print("%d nota(s) de R$ 2.00" % notas2)
print("MOEDAS:")
print("%d moeda(s) de R$ 1.00" % moedas100)
print("%d moeda(s) de R$ 0.50" % moeda50)
print("%d moeda(s) de R$ 0.25" % moeda25)
print("%d moeda(s) de R$ 0.10" % moeda10)
print("%d moeda(s) de R$ 0.05" % moeda5)
print("%d moeda(s) de R$ 0.01" % moeda1)