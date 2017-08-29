import sys

linha1 = sys.stdin.readline()
linha2 = sys.stdin.readline()

linha1 = ''.join([c for c in linha1 if c.isdigit() or c == '.'])
linha2 = ''.join([c for c in linha2 if c.isdigit() or c == '.'])

cpf = linha1[:11]
linha1 = linha1[11:]

if '.' in linha1:
    linha1 = linha1[:linha1.index('.')+3]

if '.' in linha2:
    linha2 = linha2[:linha2.index('.') + 3]

print("cpf %s" % str(cpf))
print("%.2f" % (float(linha1)+float(linha2)))