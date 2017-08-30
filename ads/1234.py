while True:
    try:
        s = input()
        maiuscula = True
        new_s = []
        for c in s:
            if len(c.strip()) > 0:
                if maiuscula:
                    c = c.upper()
                    maiuscula = False
                else:
                    c = c.lower()
                    maiuscula = True

            new_s.append(c)

        print("".join(new_s))
    except(EOFError):
        break