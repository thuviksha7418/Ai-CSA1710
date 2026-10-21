
from itertools import permutations

letters = "SENDMORY"
digits = "0123456789"

for p in permutations(digits, len(letters)):
    d = dict(zip(letters, p))

    if d['S'] == '0' or d['M'] == '0':
        continue

    send = int(''.join(d[x] for x in "SEND"))
    more = int(''.join(d[x] for x in "MORE"))
    money = int(''.join(d[x] for x in "MONEY"))

    if send + more == money:
        print("SEND =", send)
        print("MORE =", more)
        print("MONEY =", money)
        break
