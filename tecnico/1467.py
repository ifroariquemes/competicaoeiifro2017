try:
    x = input()
    d = {0:"A",1:"B",2:"C"}
    while x:
        l = [int(i) for i in x.split(" ")]
        if sum(l) == 0 or sum(l) == 3:
            print('*')
        elif sum(l) == 1:
            print(d[l.index(1)])
        elif sum(l) == 2:
            print(d[l.index(0)])

        x = input()
except EOFError:
    pass