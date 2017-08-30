d = {'tesoura' : ['papel', 'lagarto'], 'papel' : ['pedra', 'Spock'],
     'pedra' : ['tesoura', 'lagarto'], 'lagarto' : ['Spock', 'papel'], 'Spock' : ['tesoura', 'pedra']}

n = int(input())
for i in range(n):
     line = input().split(" ")

     if line[0] == line[1]:
         print("Caso #%d: De novo!" % (i+1,))
     elif line[1] in d[line[0]]:
         print("Caso #%d: Bazinga!" % (i+1,))
     else:
         print("Caso #%d: Raj trapaceou!" % (i+1,))